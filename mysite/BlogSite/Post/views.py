from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, 'home.html')


def about_me(request):
    return render(request, 'me.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'all_post_list': posts})


def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'single_post.html', {'post': post})
