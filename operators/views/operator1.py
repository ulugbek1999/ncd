from django.shortcuts import render
from django.views import View

from employee.model.employee import Employee
from operators.mixins import Operator1Mixin
from operators.models import Operator


class Operator1(View, Operator1Mixin):
    def get(self, request):
        context = {
            "register_number": request.user.operator.get_register_number
        }
        return render(request, 'operators/1/operator1.html', context)


class Operator1Stat(Operator1Mixin, View):
    def get(self, request):
        qs = Employee.objects.filter(group_id=request.user.operator1.id).values(
            'full_name_en', 'full_name_ru', 'passport_serial', 'passport_given_date', 'passport_expires',
            'passport_image', 'birth_date', 'birth_place', 'living_address_ru', 'gender', 'inn', 'phone', 'email',
            'register_number'
        )
        context = {
            "employees": qs,
        }
        return render(request, 'operators/1/stat.html', context)
