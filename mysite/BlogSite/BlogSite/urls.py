from django.contrib import admin
from django.urls import path, include
from Post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about-me/', views.about_me, name='about-me'),
    path('post-list/', views.post_list, name='post-list'),
    path('single-post/<post_id>/', views.single_post, name='single-post'),
    path('', include('account.urls')),
    path('', include('django.contrib.auth.urls')),
]
