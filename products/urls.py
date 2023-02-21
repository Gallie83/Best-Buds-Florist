from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collections, name="collections"),
    path('<int:product_id>/', views.product_details, name="product_details"),
    path('products/', views.products, name="products"),
    path('add/', views.add_product, name="add_product"),
]
