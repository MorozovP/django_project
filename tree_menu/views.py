from django.shortcuts import render
from .models import Tag


def menu(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'tree_menu/menu.html', context)