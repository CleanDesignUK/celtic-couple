from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Custom views
    path('list/', views.blog_list_view, name='blog_list'),  # /cms/blog/list/
    path('post/<int:pk>/', views.blog_detail_view, name='blog_detail'),  # /cms/blog/post/<pk>/
]
