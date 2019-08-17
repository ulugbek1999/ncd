from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from directory.models import EducationType, Language
from employee.model.employee import Employee
from operators.mixins import Operator3Mixin


class Operator3(Operator3Mixin, View):
    def get(self, request):
        if not self.employee:
            return HttpResponseRedirect(reverse('operator:3.employees'))
        context = {
            "employee": self.employee,
            'languages': Language.objects.all(),
            'education_types': EducationType.objects.all(),
        }
        return render(request, 'operators/3/operator3.html', context)


class Operator3Operator2Empolyees(Operator3Mixin, View):
    def get(self, request):
        qs = Employee.objects.search_filter(self.employees, request)
        context = {
            'employees': qs,
            'params': request.GET
        }
        return render(request, 'operators/3/operator2_employees.html', context)
