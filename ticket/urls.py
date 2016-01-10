# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #FIXME: tel que c'est fait maintenant dans treeview.js
    url(r'^get_node/(?P<node_id>.*)$', views.get_node),
    url(r'^rename_node/node_id/(?P<node_id>.*)/new_title/(?P<new_title>.*)$', views.rename_node),
    url(r'^get_content/(?P<node_id>.*)$', views.get_content),
    url(r'^create_node/parent_id/(?P<parent_id>.*)/title/(?P<title>.*)$', views.create_node),
    url(r'^delete_node/node_id/(?P<node_id>.*)$', views.delete_node),
    url(r'^move_node/node_id/(?P<node_id>.*)/parent_id/(?P<parent_id>.*)$', views.move_node),
#    url(r'^save_node$', views.save_node),
]
