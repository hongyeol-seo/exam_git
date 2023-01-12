from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by("-pk")
    # - pk값 내림차순 정렬

    return render(request, 'blog/index.html', {
        'posts': posts
    })


def single_post_page(request, value):
    post = Post.objects.get(pk=value)

    return render(
        request,
        "blog/single_post_page.html",
        {
            'post': post,
        }
    )

# Create your views here.
