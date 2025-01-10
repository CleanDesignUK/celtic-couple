# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'  # Added namespace

urlpatterns = [
    path('', views.blog_list_view, name='blog_list'),
    path('<int:pk>/', views.blog_detail_view, name='blog_detail'),
]
