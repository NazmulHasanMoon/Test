from django.urls import path
from account import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('logged-user/',views.logged_user,name='logged-user'),
]