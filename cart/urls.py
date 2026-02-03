from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:item_id>/', views.increase_cart_quantity, name='increase_cart'),
    path('decrease/<int:item_id>/', views.decrease_cart_quantity, name='decrease_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]