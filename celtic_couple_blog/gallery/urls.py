# gallery/urls.py

from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('shetland-2024-road-trip/', views.shetland_2024_view, name='shetland_2024'),
    path('orkney-2021/', views.orkney_2021_view, name='orkney_2021'),
    path('shetland-2021/', views.shetland_2021_view, name='shetland_2021'),
    path('normandy-beaches-2023/', views.normandy_beaches_2023_view, name='normandy_beaches_2023'),
]
