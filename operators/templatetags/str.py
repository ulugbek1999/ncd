from django import template

register = template.Library()


@register.filter(name='str')
def id_to_str(id):
    return str(id)


@register.simple_tag()
def get_group(operator):
    if hasattr(operator, 'group_operator1'):
        return operator.group_operator1.id
    elif hasattr(operator, 'group_operator2'):
        return operator.group_operator2.id
    elif hasattr(operator, 'group_operator3'):
        return operator.group_operator3.id
    elif hasattr(operator, 'group_operator4'):
        return operator.group_operator4.id
    return 0
