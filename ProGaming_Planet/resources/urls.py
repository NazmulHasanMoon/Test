from django.urls import path
from resources import views


urlpatterns = [
    path('basic/', views.basic, name='basic'),
    path('pro_lang/', views.programming_language, name='pro_lang'),
    path('index/', views.index, name='index'),
    path('sort_search/', views.sort_search, name='sort_search'),
    path('ds/', views.ds, name='ds'),

]