from django import template

from employer.models import EmployerEmployee

register = template.Library()


@register.simple_tag(takes_context=True)
def is_in_bookmark(context, employee_id):
    p = EmployerEmployee.objects.filter(employer=context['request'].user.employer, employee_id=employee_id)
    return True if p.count() == 1 else False
