from django.shortcuts import render, redirect, reverse
from .models import Post, Comment
from .forms import PostForm

from django.contrib import messages


def view_posts(request):
    """ View to return index page """
    template = 'community/view_posts.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Added!')
            return redirect(reverse('view_posts'))
        else:
            messages.error(request, "Post couldn't be added. Please check over your form.")
    else:
        form = PostForm()
    template = 'community/add_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
