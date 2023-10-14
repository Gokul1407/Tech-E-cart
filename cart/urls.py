from django.urls import path
from cart import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_item/<int:product_id>/',views.remove_item,name='remove_item')
]
