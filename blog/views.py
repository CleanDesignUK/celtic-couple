from django.shortcuts import render, get_object_or_404
from .models import BlogPage  # Using your Wagtail BlogPage model

def blog_list_view(request):
    """
    List all blog posts using Wagtail's BlogPage model.
    """
    posts = BlogPage.objects.live().order_by('-date')  # Fetch published posts ordered by date
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail_view(request, pk):
    """
    Show the details of a single blog post by primary key.
    """
    post = get_object_or_404(BlogPage, pk=pk)  # Fetch post by primary key
    return render(request, 'blog/blog_detail.html', {'post': post})
