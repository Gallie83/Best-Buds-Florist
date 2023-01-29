from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name="products"),
    path('bouquets/', views.bouquets, name="bouquets"),
    path('flowers/', views.flowers, name="flowers"),
    path('indoor_plants/', views.indoor_plants, name="indoor_plants"),
]
