from django import template
from tree_menu.models import Item


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu():
    items = Item.objects.all()
    return {'items': items}