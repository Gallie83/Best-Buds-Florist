from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def blogposts(request):
    """ Returns Blog Posts section """

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/best_blogs.html', context)
