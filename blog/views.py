# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

# 회원가입 및 로그인 구현 부분 
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.core.context_processors import csrf
from django.contrib.auth import get_user_model


def register(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return render_to_response('registration/registration_complete.html')

     else:
         form = UserCreationForm()
     token = {}
     token.update(csrf(request))
     token['form'] = form

     return render_to_response('registration/registration_form.html', token)



def loggedin(request):
    return render_to_response('registration/loggedin.html',{'username': request.user.username})

############

def index(request):
    user = request.user
    posts = Post.objects.all().order_by('-published_date')
    context = {'posts' : posts, 'current_user' : user}
    return render(request, 'blog/index.html', context)

@login_required
def write(request):
    post = Post()
    post.author = request.user
    post.title = request.POST['title']
    post.text = request.POST['content']
    post.published_date = timezone.now()
    post.save()
    
    return redirect('blog.views.index')
    
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    
    return redirect('blog.views.index')
    
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.author = request.user
        post.title = request.POST['title']
        post.text = request.POST['content']
        post.published_date = timezone.now()
        post.save()
        return redirect('blog.views.index')
    else:
        context={'post' : post}
        return render(request, 'blog/post_edit.html', context)