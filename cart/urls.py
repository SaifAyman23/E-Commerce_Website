from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    path('',views.cart,name='cart'),
    path('add/<int:item_id>/',views.add_item,name='add_item'),
    path('remove/<int:item_id>/',views.remove_cart_item,name='remove_cart_item'),
    path('removecart/<int:item_id>/',views.remove_cart,name='remove_cart'),
    
]
