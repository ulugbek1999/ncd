from django import template

from partner.models import PartnerEmployee

register = template.Library()


@register.simple_tag(takes_context=True)
def is_in_bookmark(context, employee_id):
    p = PartnerEmployee.objects.filter(partner=context['request'].user.partner, employee_id=employee_id)
    return True if p.count() == 1 else False
