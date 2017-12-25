from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post/list.html',{'posts': posts})


def post_detail(request,post):
    post =Post.objects.get(id=post)
    return render(request,'post/detail.html',{'post': post})
