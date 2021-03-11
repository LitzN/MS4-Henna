from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Comment
from profiles.models import UserProfile
from .forms import PostForm, CommentForm

from django.contrib import messages


def view_posts(request):
    """ View to return index page """
    template = 'community/view_posts.html'
    posts = Post.objects.all()
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Added!')
        else:
            messages.error(request, "Post couldn't be added. Please check over your form.")
    else:
        form = CommentForm()
    context = {
        'posts': posts,
        'form': form,
        'comments': comments,
    }
    return render(request, template, context)


def add_post(request):
    user = get_object_or_404(UserProfile, user=request.user)
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
        'user': user,
    }
    return render(request, template, context)


def delete_comment(request, comment_id):
    user = get_object_or_404(UserProfile, user=request.user)
    comment = get_object_or_404(Comment, id=comment_id)
    if user == comment.user_profile:
        comment.delete()
        messages.success(request, 'Comment Deleted!')
    else:
        messages.error(request, 'Sorry, you can only delete your own comments.')
    return redirect(reverse('view_posts'))


def delete_post(request, post_id):
    user = get_object_or_404(UserProfile, user=request.user)
    post = get_object_or_404(Post, id=post_id)
    if user == post.user_profile:
        post.delete()
        messages.success(request, 'Post Deleted!')
    else:
        messages.error(request, 'Sorry, you can only delete your own posts.')
    return redirect(reverse('view_posts'))
