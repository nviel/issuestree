$(function () {
  $(window).resize(function () {
    var h = Math.max($(window).height() - 0, 420);
    $('#container, #data, #tree, #data .content').height(h).filter('.default').css('lineHeight', h + 'px');
  }).resize();

  $('#tree')
    .jstree({
      'core' : {
        'data' : {
          'url' : function(node){
            if (node.id === '#') {
              id = 0;
            }else{
              id =node.id;
            }
            return "get_node/" + id;
          }
        },
        'check_callback' : function(o, n, p, i, m) {
          // don't hunderstand what is parameter
          if(m && m.dnd && m.pos !== 'i') { return false; }
          // copy or move a node where it already is is forbidden.
          if(o === "move_node" || o === "copy_node") {
            if(this.get_node(n).parent === this.get_node(p).id) { return false; }
          }
          return true;
        },
        'force_text' : true,
        'themes' : {
          'responsive' : false,
          'variant' : 'small',
          'stripes' : true
        }
      },
      'sort' : function(a, b) { // tri sur l'ordre alphabetique
        return this.get_type(a) === this.get_type(b) ? (this.get_text(a) > this.get_text(b) ? 1 : -1) : (this.get_type(a) >= this.get_type(b) ? 1 : -1);
      },
      'contextmenu' : {
        'items' : function(node) {
           var tmp = $.jstree.defaults.contextmenu.items();
           tmp.create.action = function (data) {
             var inst = $.jstree.reference(data.reference),
             obj = inst.get_node(data.reference);
             inst.create_node(obj, { type : "default" }, "last", function (new_node) {
               setTimeout(function () { inst.edit(new_node); },0);
             });
           };
          // //FIXME: le shortcut ne fonctionne pas?!
          // tmp.create.shortcut = 113;
          // tmp.create.shortcut_label = 'F2';
          // if(this.get_type(node) === "file") {
          //   delete tmp.create;
          // }
          return tmp;
        }
      },
      // end of contextmenu

      'types' : {
        'default' : { 'icon' : 'folder' },
        'file' : { 'valid_children' : [], 'icon' : 'file' }
      },
      'unique' : {
        'duplicate' : function (name, counter) {
          return name + ' ' + counter;
        }
      },
      'plugins' : ['state','dnd','sort','types','contextmenu','unique']
    })
    .on('delete_node.jstree', function (e, data) {
      $.get('delete_node/node_id/' + data.node.id)
        .fail(function () {
          data.instance.refresh();
        });
    })
    .on('create_node.jstree', function (e, data) {
      console.log("CREATE_NODE");
      $.get('create_node/parent_id/' + data.node.parent + '/title/' + data.node.text)
        .done(function (d) {
          data.instance.set_id(data.node, d.id);
        })
        .fail(function () {
          data.instance.refresh();
        });
    })
    .on('rename_node.jstree', function (e, data) {
      $.get('rename_node/node_id/' + data.node.id + '/new_title/' + data.text, {})
        .done(function (d) {
          data.instance.set_id(data.node, d.id);
        })
        .fail(function () {
          data.instance.refresh();
        });
    })
    .on('move_node.jstree', function (e, data) {
      $.get('move_node/node_id/' + data.node.id + '/parent_id/' + data.parent)
        .done(function (d) {
          //data.instance.load_node(data.parent);
          data.instance.refresh();
        })
        .fail(function () {
          data.instance.refresh();
        });
    })
    .on('copy_node.jstree', function (e, data) {
      $.get('actions.php?operation=copy_node', { 'id' : data.original.id, 'parent' : data.parent })
        .done(function (d) {
          //data.instance.load_node(data.parent);
          data.instance.refresh();
        })
        .fail(function () {
          data.instance.refresh();
        });
    })
});
