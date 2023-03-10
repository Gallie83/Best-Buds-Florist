from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collections, name="collections"),
    path('<int:product_id>/', views.product_details, name="product_details"),
    path('products/', views.products, name="products"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
    path('delete/<int:product_id>/', views.delete_product, name="delete_product"),
    path('delete_review/<int:review_id>/',
         views.delete_review, name="delete_review"),
]
