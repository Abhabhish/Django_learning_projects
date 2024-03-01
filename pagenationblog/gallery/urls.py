from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name = 'product_list'),
    path('details/<int:id>/',views.product_details,name='product_details'),
    path('delete/<int:id>/',views.product_delete,name = 'product_delete'),
    path('edit/<int:id>/',views.edit_product,name = 'edit_product'),
]