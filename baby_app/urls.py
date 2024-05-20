from django.urls import path
from . import views

urlpatterns = [
    path('', views.babyhome, name='baby'),
    path('addbaby', views.addbaby, name='addbaby'),
    path('editbaby/<int:baby_id>', views.editbaby, name='editbaby'),
    path('deletebaby/<int:baby_id>', views.deletebaby, name='deletebaby'),
    path('viewbaby/<int:baby_id>', views.viewbaby, name='viewbaby'),
    path('searchbaby', views.searchbaby, name='searchbaby'),
    path('pickup', views.pickup, name='pickup'),
    path('store', views.store_view, name='store'),
    path('transactions', views.transaction_view, name='transactions'),
    path('additem', views.add_Item, name='additem'),
    path('edititem<int:item_id>', views.edit_item, name='edititem'),
    path('deleteitem<int:item_id>', views.delete_item, name='deleteitem'),
    path('dollpay', views.doll_pay, name='dollpay'),
    path('duty', views.dutyadd, name='duty'),
]