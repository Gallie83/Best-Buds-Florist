from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('weddings/', views.weddings, name="weddings"),
    path('funerals/', views.funerals, name="funerals"),
]
