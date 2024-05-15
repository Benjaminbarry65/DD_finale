from django.urls import path
from . import views

urlpatterns = [
    path('', views.babyhome, name='baby'),
    path('addbaby', views.addbaby, name='addbaby'),
    path('editbaby/<int:baby_id>', views.editbaby, name='editbaby'),
    path('deletebaby/<int:baby_id>', views.deletebaby, name='deletebaby'),
    path('viewbaby/<int:baby_id>', views.viewbaby, name='viewbaby'),
    path('pickupbaby', views.pickupbaby, name='pickupbaby'),
    path('pickup/<int:baby_id>', views.pickup, name='pickup'),
    path('store', views.store_view, name='store'),
    path('transactions', views.transaction_view, name='transactions'),
    path('additem', views.add_Item, name='additem'),
]