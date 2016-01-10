# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Ticket

import json

#-------------------------------------------------------------------------------
def index(request):
    #context = RequestContext(request, {'nom_var_in_template': valeur,... ,})
    context = {}
    return render(request, 'ticket/index.html', context)

#-------------------------------------------------------------------------------
# Retourne les éléments du noeud nécessaires pour jstree
#-------------------------------------------------------------------------------
def get_node(request, node_id = "0"):
    #node = Ticket.objects.get(id = node_id)
    children_q = Ticket.objects.filter(parent = node_id)
    children = []
    for c in children_q:
        d = {"id" : c.id, "text": c.title, "icon":"folder"}
        grd_child_q = Ticket.objects.filter(parent = c.id)
        if (len(grd_child_q)>0):
            d["children"]=True
        children.append(d)

    #n = {"id" : node.id, "text": node.title, "icon":"folder", "children":children }
    return HttpResponse(json.dumps(children), content_type="application/json")

#-------------------------------------------------------------------------------
# FIXME: Enregistre en BDD l'état d'un noeud modifié dans la view tree.
#-------------------------------------------------------------------------------
def save_node(request):
    return HttpResponse("Node saved")

#-------------------------------------------------------------------------------
# renomme le noeud et sauvegarde le nouveau nom en base
# FIXME: ce controleur devrait être généralisé en update_node (à faire lors de
#        la bascule vers une api REST)
#-------------------------------------------------------------------------------
def rename_node(request, node_id, new_title = "new node"):
    node = Ticket.objects.get(id = node_id)
    node.title = new_title
    node.save()
    return HttpResponse("Node renamed!")


# FIXME: retourne les infos du ticket. A faire en vrai quand il y aura vraiment
#        du contenu...
#-------------------------------------------------------------------------------
def get_content(request, node_id = "#"):
    return HttpResponse("Contenu du ticket [" + node_id + "]" )

# Créee un nouveau noeud en base et retourne son identifiant
#-------------------------------------------------------------------------------
def create_node(request, parent_id, title):
    try:
        parent_node = Ticket.objects.get(id=parent_id)
    except Exception as e:
        return HttpResponse(str(e), status = 400)

    node = Ticket(parent = parent_node, title = title)
    node.save()
    return HttpResponse(str(node.id))

# Supprime un noeud
# FIXME: ne supprime que le noeud désigné. Il est probable que le comportement
# souhaité à terme sera de supprimer également tous les enfants récurcivement.
#-------------------------------------------------------------------------------
def delete_node(request, node_id):
    try:
        node = Ticket.objects.get(id=node_id)
    except Exception as e:
        return HttpResponse(str(e), status = 400)

    node.delete()
    return HttpResponse(str(node.id))

# Déplace un noeud dans l'arbre
#-------------------------------------------------------------------------------
def move_node(request, node_id, parent_id):
    try:
        parent_node = Ticket.objects.get(id=parent_id)
        node = Ticket.objects.get(id=node_id)
    except Exception as e:
        return HttpResponse(str(e), status = 400)

    node.parent = parent_node
    node.save()

    return HttpResponse(str(node.id))
