from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name="account"),
    path('profile_picture', views.profile_picture, name="profile_picture"),
    path('order_history/<order_number>',
         views.order_history, name="order_history"),
]
