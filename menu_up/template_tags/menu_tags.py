from django import template
from ..models import Menu


register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def menu(context):
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by("-priority").all()}