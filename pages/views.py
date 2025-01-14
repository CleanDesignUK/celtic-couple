# pages/views.py

from django.shortcuts import render



def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def work_with_us_view(request):
    return render(request, 'pages/work_with_us.html')
