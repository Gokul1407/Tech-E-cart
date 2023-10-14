from django.urls import path
from store import views


urlpatterns = [
    path('',views.store,name='store'),
    path('category_sort/<slug:category_slug>/',views.category_sort, name='category_sort'),
    path('product_details/<slug:product_slug>/',views.product_details,name='product_details'),
]
          