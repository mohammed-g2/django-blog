from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from .forms import UpdatePostForm, DeletePostForm
from .util import paginate_posts


def home(request):
    posts_per_page = 5
    current_page = request.GET.get('page', 1)
    p = paginate_posts(current_page, posts_per_page)

    return render(request, 'blog/home.html', {
        'pages': p['pages'],
        'page_obj': p['page_obj'],
        'title': 'Home Page',
        'page_header': None,
        'view': 'blog:home'
    })


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts_per_page = 5
    current_page = request.GET.get('page', 1)
    p = paginate_posts(current_page, posts_per_page, user)

    return render(request, 'blog/home.html', {
        'pages': p['pages'],
        'page_obj': p['page_obj'],
        'title': user.username,
        'page_header': f'Posts by: { user.username }',
        'view': 'blog:user_posts',
        'targeted_user': user
    })


def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = DeletePostForm(initial={'id': post.id})
    return render(request, 'blog/post.html', {
        'post': post,
        'form': form,
        'title': post.title
    })


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def terms(request):
    return render(request, 'blog/terms.html', {'title': 'Terms'})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = UpdatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            return redirect('blog:post', id=post.id)
    else:
        form = UpdatePostForm()
    return render(request, 'blog/edit_post.html', {'title': 'Create post', 'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('forbidden')
    
    if request.method == 'POST':
        form = UpdatePostForm(request.POST)
        if form.is_valid():
            updated_post = form.save(commit=False)
            post.title = updated_post.title
            post.content = updated_post.content
            post.save()
            return redirect('blog:post', id=post.id)
    else:
        form = UpdatePostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'title': 'Post Editing', 'form': form})


@login_required
def delete_post(request):
    if request.method == 'POST':
        form = DeletePostForm(request.POST)
        post = get_object_or_404(Post, id=form.data.get('id'))
        if request.user != post.author:
            return redirect('forbidden')
        if form.is_valid():
            post.delete()
            messages.success(request, 'post deleted')
    return redirect('blog:home')
