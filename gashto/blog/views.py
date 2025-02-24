from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}

    return render(
        request, 'Website/Home.html', context
    )


def about_us(request):
    context = {}

    return render(
        request, 'Website/AboutUs.html', context
    )


def contact_us(request):
    context = {}

    return render(
        request, 'Website/ContactUs.html', context
    )


@login_required
def new_post(request):
    if request.method == 'POST':
        pass
        # author =
        # title
        # subtitle
        # status
        # slug
        # category
        # publish_date
        # created_date
        # upadted_date
        # body

    else:
        context = {
        }

        return render(
            request, 'Blog/PostNew.html', context)


def post_list(request):

    if request.method == 'GET':
        posts = Post.publishedObjects.get_published_posts()
        context = {
            'posts': posts
        }
        return render(
            request, 'Blog/PostList.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'Blog/PostDetail.html',
                  {'post': post})
