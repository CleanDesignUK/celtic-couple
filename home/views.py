# home/views.py

from django.shortcuts import render
from blog.models import BlogPage

def home_view(request):
    # Attempt to fetch the latest blog post by date
    featured_post = (
        BlogPage.objects.live()
        .order_by('-date')
        .first()
    )

    context = {
        'featured_post': featured_post,
    }
    return render(request, 'home/home_page.html', context)
