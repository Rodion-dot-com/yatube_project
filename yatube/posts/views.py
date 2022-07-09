from django.shortcuts import get_object_or_404, render

from .models import Group, Post

MAX_SAMPLE_SIZE = 10


def index(request):
    """Renders the main page of the site."""
    posts = Post.objects.select_related('author', 'group')[:MAX_SAMPLE_SIZE]
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Renders posts from a specific community."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author', 'group')[:MAX_SAMPLE_SIZE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
