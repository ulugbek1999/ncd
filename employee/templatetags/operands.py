from django import template

register = template.Library()


@register.simple_tag(name='range_number')
def range_number(num1, num2):
    return range(num1 - num2)


@register.simple_tag(name='minus_numbers')
def minus_numbers(num1, num2):
    return num1 - num2.stop


@register.simple_tag(name='plus_numbers')
def plus_numbers(num1, num2):
    return num1 + num2
