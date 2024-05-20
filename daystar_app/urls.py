from django.urls import path
from . import views


urlpatterns = [
    path('', views.sitter_home, name="sitter"),
    path('add', views.addsitter, name="addsitter"),
    path('edit/<int:sitter_id>', views.editsitter, name="editsitter"),
    path('delete/<int:sitter_id>', views.deletesitter, name="deletesitter"),
    path('view/<int:sitter_id>/', views.viewsitter, name="viewsitter"),
    path('searchsitter', views.searchsitter, name="searchsitter"),
]