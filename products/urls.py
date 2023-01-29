from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products, name="products"),
    path('bouquets/', views.Bouquets, name="bouquets"),
    path('flowers/', views.Flowers, name="flowers"),
]
