from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import BlogPost
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def add_post(request):
    """ Add a new post to blog """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry! Only authorised users have access to this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post Added!')
            return redirect(reverse('blog_posts'))
        else:
            print(form.errors)
            messages.error(
                request, 'Failed to add post! Ensure the form is valid')

    form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)
