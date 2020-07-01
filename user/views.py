from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout, login as django_login, authenticate 
from django.contrib import messages
from .forms import (
    UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserLoginForm, PasswordResetForm)


def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created successfly, you can login now')
            return redirect('user:login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', {'form': form, 'title': 'register'})



def login(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, 
                username=form.data.get('username'), 
                password=form.data.get('password'))
            if user:
                django_login(request, user)
                return redirect('blog:home')
        messages.warning(request, 'incorrect username or password')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'login'})


@login_required
def logout(request):
    django_logout(request)
    return redirect('blog:home')


def profile(request, username):
    user = get_object_or_404(User, username=username)

    if user != request.user:
        return render(request, 'user/profile.html', {'title': 'profile',
            'profile_owner': user})

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, 
            instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'account info updated')
            return redirect('user:profile', username=username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {
        'title': 'profile',
        'user_form': user_form,
        'profile_form': profile_form,
        'profile_owner': request.user
    })