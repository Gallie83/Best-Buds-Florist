from django.urls import path
from . import views

urlpatterns = [
    path('blog_posts/', views.blog_posts, name="blog_posts"),
    path('add_post/', views.add_post, name="add_post"),
    path('<slug:slug>/', views.post_details, name="post_details"),
]
