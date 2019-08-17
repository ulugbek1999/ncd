from django import template

from employee.model.employee import EmployeeCountry

register = template.Library()


@register.simple_tag(name='check_for_country')
def check_for_country(employee_id, country_id):
    return True if EmployeeCountry.objects.filter(
        employee_id=employee_id,
        country_id=country_id).count() > 0 else False
