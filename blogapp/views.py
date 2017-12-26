from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):

    # return render(request,'post/list.html',{'posts': posts})
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/list.html', {'page': page,
                                                   'posts': posts})


def post_detail(request,slug):
    post =Post.objects.get(slug=slug)
    return render(request,'post/detail.html',{'post': post})
