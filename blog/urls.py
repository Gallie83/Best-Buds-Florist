from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.blogposts, name="blogposts"),
]
