# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('work-with-us/', views.work_with_us_view, name='work_with_us'),
]
