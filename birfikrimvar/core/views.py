from django.shortcuts import render
from posts.models import Post


def home(request):
    """
    Home page view
    """
    posts = Post.objects.all()[:10]  # Get the 10 most recent posts
    return render(request, 'core/home.html', {'posts': posts})


def about(request):
    """
    About page view
    """
    return render(request, 'core/about.html')