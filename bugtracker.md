[   ] faire communiquer les vues entre elles
  [ok?] lister les events qui doivent déclencher une mise à jour
    [ * ] ticket_select
      [ * ] met à jour la vue de détail avec le ticket sélectionné
      [ * ] déplie la tree_view et sélectionne le ticket sélectionné
      [ ? ] impact sur la vue liste?
    [ * ] ticket_change: pour toutes les vues : charge les changements du ticket en base (s'il est visible dans la vue.)
  [   ] comment organiser la gestion des événements?

[...] Vue tree
  [...] menu contextuel
    [ok!] déploiement de l'arbre avec ajax (get_content)
    [ok!] renommer un noeud (rename_node)
    [...] créer un noeud
      [ok ] URL, controleur, tree_view
      [   ] changer le nom du noeud
    [ok!] déplacer un noeud
    [   ] le raffraichissement complet de l'arbre à l'occasion du déplacement d'un noeud est déplaisant.
    [...] supprimer un noeud
      [ok!] sans précautions
      [] avec message de confirmation
      [] avec tous les enfants récursivement

  [   ] Affichage
    [   ] il manque les pointillés verticaux reliants le père à ses enfants (autre que le premier)

[   ] Vue de détail
    [   ] afficher le contenu d'un noeud dans la vue détail (get_content)
      [   ] dans un premier temps juste le node_id.
        [ok?] implémentation de get_content trivial dans views.py
        [   ] affichage dans la vue détail
        [   ] écouter les événements des autres vues pour mettre à jour l'affichage.

[   ] Vue liste

[   ] Vue document

[   ] Développement
  [   ] le serveur devrait exposer une API de type REST.
    [ ? ] Pourquoi? Quel est le gain?
    [ * ] Il faudrait utiliser les méthodes GET/POST/UPDATE
    [ * ] Il existe une extension de django pour la gestion du REST (django-rest-framework)
    [ ? ] Ne pas oublier qu'il ne s'agit que d'un prototype pour évaluer les nouveaux principes.
    [ X ] Le controleur rename_node prend le parametre new_title. Ce serait plus homogène si c'était title.
    [ X ] Le controleur rename_node devrait sans doute être update_node avec la liste des champs/valuers à mettre à jour.