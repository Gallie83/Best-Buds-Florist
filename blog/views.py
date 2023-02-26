from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def blog_posts(request):
    """ Returns Blog Posts section """

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/best_blogs.html', context)


def post_details(request, slug):
    """ Shows single post with all details and comments """

    post = BlogPost.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post.html', context)
