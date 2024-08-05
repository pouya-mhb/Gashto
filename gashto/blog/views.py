from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}

    return render(
        request, 'Home.html', context
    )


def about_us(request):
    context = {}

    return render(
        request, 'AboutUs.html', context
    )


def contact_us(request):
    context = {}

    return render(
        request, 'ContactUs.html', context
    )


posts = Post.objects.all()
users = User.objects.all()

global_context = {
    'posts': posts,
    'users': users
}


@login_required
def new_post(request):
    # contains title, body,status
    # auto slug
    # auto date and time
    # auto autor - if user/autor is not none and @login_required
    pass


def post_list(request):
    # user should be able to add new post

    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(
            request, 'PostList.html', context)

    if request.method == 'POST':
        user = User.object.get(username='admin')  # an instance from the User
        title = 'a good day in mexico'
        slug = 'a-good-day-in-mexico'
        body = 'this is a good day in mexico '
        author = user

        # an instance from Post model to save
        new_post = Post.objects.create(user, title, slug, body, author)
        new_post.save()

        new_post_context = {

            # author
            # status
            # title
            # body
            # date_published

        }

        return render(
            request, 'PostList.html',)

    else:
        pass


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'PostDetail.html',
                  {'post': post})
