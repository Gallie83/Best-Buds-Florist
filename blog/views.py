from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import CommentForm
from django.contrib import messages


def blog_posts(request):
    """ Returns Blog Posts section """

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/best_blogs.html', context)


def post_details(request, slug):
    """ 
    Shows single post with all details and comments
    and allows user to leave comment 
    """

    post = BlogPost.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_id = request.user.id
            comment.save()
            messages.success(request, 'Thanks for your comment!')
            return redirect('post_details', slug=post.slug)

    else:
        form = CommentForm(request.POST)

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/blog_post.html', context)
