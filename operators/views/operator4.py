from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from directory.models import Country, City, EducationType, District, Language as DLanguage
from employee.model.employee import Employee
from operators.mixins import Operator4Mixin


class Operator4(Operator4Mixin, View):
    def get(self, request):
        if not self.employee:
            return HttpResponseRedirect(reverse('operator:4.employees'))
        context = {
            "employee": self.employee,
            'countries': Country.objects.all()
        }
        return render(request, 'operators/4/operator4.html', context)


class Operator4Operator3Empolyees(Operator4Mixin, View):
    def get(self, request):
        qs = Employee.objects.search_filter(self.employees, request)
        context = {
            'employees': qs,
            'params': request.GET
        }
        return render(request, 'operators/4/operator3_employees.html', context)


class EmployeeUpdateOP3(Operator4Mixin, DetailView):
    pk_url_kwarg = 'id'
    model = Employee
    template_name = 'operators/4/employee_update_3.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        context["educations"] = EducationType.objects.all()
        context["districts"] = District.objects.all()
        context["languages"] = DLanguage.objects.all()
        return context
