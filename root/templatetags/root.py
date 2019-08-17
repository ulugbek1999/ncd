from django import template

register = template.Library()


@register.filter()
def range(a):
    return range(15, 65)
