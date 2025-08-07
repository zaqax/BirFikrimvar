from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment, Like
from .forms import PostForm, CommentForm


def post_list(request):
    """
    View for listing all posts
    """
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    View for displaying a specific post with its comments
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    # Check if current user has liked the post
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = Like.objects.filter(post=post, user=request.user).exists()
    
    # Handle comment form
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Yorumunuz başarıyla eklendi.')
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_has_liked': user_has_liked,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    """
    View for creating a new post
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Fikriniz başarıyla paylaşıldı!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'posts/post_form.html', {'form': form, 'title': 'Fikir Paylaş'})


@login_required
def post_edit(request, pk):
    """
    View for editing an existing post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user is the author of the post
    if post.user != request.user:
        messages.error(request, 'Bu fikri düzenleme yetkiniz yok.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fikriniz başarıyla güncellendi!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'posts/post_form.html', {'form': form, 'title': 'Fikir Düzenle'})


@login_required
def post_delete(request, pk):
    """
    View for deleting a post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user is the author of the post
    if post.user != request.user:
        messages.error(request, 'Bu fikri silme yetkiniz yok.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Fikriniz başarıyla silindi.')
        return redirect('home')
    
    return render(request, 'posts/post_confirm_delete.html', {'post': post})


@login_required
def post_like(request, pk):
    """
    View for liking a post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user has already liked the post
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    
    if not created:
        # If the like already exists, do nothing (prevent double liking)
        pass
    
    # Redirect back to the post detail page
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


@login_required
def post_unlike(request, pk):
    """
    View for unliking a post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Try to find and delete the like
    Like.objects.filter(post=post, user=request.user).delete()
    
    # Redirect back to the post detail page
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


@login_required
def comment_delete(request, pk):
    """
    View for deleting a comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    
    # Check if the user is the author of the comment
    if comment.user != request.user:
        messages.error(request, 'Bu yorumu silme yetkiniz yok.')
        return redirect('post_detail', pk=post_pk)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Yorumunuz başarıyla silindi.')
    
    return redirect('post_detail', pk=post_pk)