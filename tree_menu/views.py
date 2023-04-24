from django.shortcuts import render, get_object_or_404

from .models import Item


def index(request):
    return render(request, 'tree_menu/index.html')


def menu(request, slug):
    menu = get_object_or_404(Item, slug=slug)
    context = {'menu': menu}
    return render(request, 'tree_menu/menu.html', context)