from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from employee.model.employee import Employee
from operators.mixins import Operator2Mixin


class Operator2(Operator2Mixin, View):
    def get(self, request):
        if not self.employee:
            return HttpResponseRedirect(reverse('operator:2.employees'))
        context = {
            "employee": self.employee,
        }
        return render(request, 'operators/2/operator2.html', context)


class Operator2Operator1Empolyees(Operator2Mixin, View):
    def get(self, request):
        qs = Employee.objects.search_filter(self.employees, request)
        context = {
            'employees': qs,
            'params': request.GET
        }
        return render(request, 'operators/2/operator1_employees.html', context)
