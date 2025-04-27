from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path ("wiki/<str:title>",views.entry,name="entry"),
    path("search/",views.search,name = "search"),
    path("new/",views.new_page,name="new"),
    path("edit/",views.edit,name="edit"),
    path("do_edit/",views.do_edit,name="do_edit"),
    path("random/",views.random,name="random")
   
]
