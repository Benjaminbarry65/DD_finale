from django.urls import path
from . import views


urlpatterns = [
    path('', views.sitter_home, name="sitter"),
    path('add', views.addsitter, name="addsitter"),
    path('edit', views.editsitter, name="editsitter"),
    path('delete', views.deletesitter, name="deletesitter"),
]