from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from blog.models import Comment, Like, Post, PostView
from blog.forms import UserPostForm
from .forms import ProfileForm, UpdateUserForm, UserForm, ProfileForm


def home(request):
    return render(request, 'appblog/home.html')


def register(request):
    form_user = UserForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        
        if form_user.is_valid() :
            user = form_user.save()
           
            login(request, user)
            messages.success(request, 'Register Successfully!')

            return redirect('home')

    context = {
        "form_user": form_user,
        
    }

    return render(request, 'appblog/register.html',context)


def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return render(request, 'appblog/logout.html')



def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfully!")
            login(request, user)
            return redirect('list')
    return render(request, 'appblog/user_login.html', {"form": form})


@login_required
def user_profile(request):
   
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'appblog/profile.html', context)

def post_update(request, id):
    post = Post.objects.get(id=id)
    form = UserPostForm(instance=post)
    if post.user == request.user:
        if request.method == "POST":
            form = UserPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully')
                return redirect('post_detail', id=id)
    else:
        messages.error(request, 'You are not allowed to update this post')
        return redirect('post_detail', id=id)
    context = {
        'update_form': form,
    }
    return render(request, 'blog/post_update.html', context)