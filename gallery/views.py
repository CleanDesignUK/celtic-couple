# gallery/views.py

from django.shortcuts import render

def gallery_view(request):
    """
    Main gallery overview page with four album cards.
    """
    return render(request, 'gallery/gallery.html')

def shetland_2024_view(request):
    """
    Gallery page for Shetland 2024 Road Trip.
    """
    return render(request, 'gallery/album_shetland_2024.html')

def orkney_2021_view(request):
    """
    Gallery page for Orkney 2021.
    """
    return render(request, 'gallery/album_orkney_2021.html')

def shetland_2021_view(request):
    """
    Gallery page for Shetland 2021.
    """
    return render(request, 'gallery/album_shetland_2021.html')

def normandy_beaches_2023_view(request):
    """
    Gallery page for Normandy Beaches 2023.
    """
    return render(request, 'gallery/album_normandy_beaches_2023.html')
