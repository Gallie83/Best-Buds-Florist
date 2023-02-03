from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collections, name="collections"),
    path('product_search/', views.product_search, name="product_search"),
    path('<product_id>', views.product_details, name="product_details"),
    path('products/', views.products, name="products"),
    path('bouquets/', views.bouquets, name="bouquets"),
    path('indoor_plants/', views.indoor_plants, name="indoor_plants"),
    path('specials/', views.specials, name="specials"),
]
