// FIXME: Ici je commente tout parce que c'est à la vue de détail d'aller chercher les infos.
//        Il faudra creuser ça quand je mettrai en place les différentes vues.
//
// <jstree object> .on('changed.jstree', function (e, data) {
//   if(data && data.selected && data.selected.length) {
//     $.get('get_content/' + data.selected.join(':'), function (d) {
//       if(d && typeof d.type !== 'undefined') {
//         $('#data .content').hide();
//         switch(d.type) {
//           case 'text':
//           case 'txt':
//           case 'md':
//           case 'htaccess':
//           case 'log':
//           case 'sql':
//           case 'php':
//           case 'js':
//           case 'json':
//           case 'css':
//           case 'html':
//             $('#data .code').show();
//             $('#code').val(d.content);
//             break;
//           case 'png':
//           case 'jpg':
//           case 'jpeg':
//           case 'bmp':
//           case 'gif':
//             $('#data .image img').one('load', function () { $(this).css({'marginTop':'-' + $(this).height()/2 + 'px','marginLeft':'-' + $(this).width()/2 + 'px'}); }).attr('src',d.content);
//             $('#data .image').show();
//             break;
//           default:
//             $('#data .default').html(d.content).show();
//             break;
//         }
//       }
//     });
//   }
//   else {
//     $('#data .content').hide();
//     $('#data .default').html('Select a file from the tree.').show();
//   }
// });
