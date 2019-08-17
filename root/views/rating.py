from django.views.generic import ListView

from employee.model.employee import Employee
from root.mixins import IsSuperUserMixin


class Ratings(IsSuperUserMixin, ListView):
    model = Employee
    template_name = "root/employee/ratings.html"
    context_object_name = "employees"
