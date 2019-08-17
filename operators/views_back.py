"""
TODO User has no operator1/2/3/4 ni fix qilish kk

TODO global: operators getting ws message from others
TODO op1: email does not work;
TODO op2:
"""

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from directory.models import Language, EducationType, Country
from employee.model.employee import Employee


class Operator1(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") or not hasattr(request.user, "operator1"):
            raise Http404
        context = {
            "register_number": request.user.operator.get_register_number
        }
        return render(request, 'operators/1/operator1.html', context)


class Operator2(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator2"):
            raise Http404
        emp = Employee.objects.get(id=request.GET.get("id"))
        context = {
            "emp_id": emp.id,
            "register_number": emp.register_number
        }
        return render(request, 'operators/2/operator2.html', context)


class Operator2Operator1Empolyees(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator2"):
            raise Http404
        if hasattr(request.user, 'operator2'):
            context = {
                'employees': Employee.objects.filter(step_finished=1, group__id=request.user.operator2.id)
            }
            return render(request, 'operators/2/operator1_employees.html', context)
        else:
            return HttpResponseRedirect("/")


class Operator3(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator3"):
            raise Http404
        emp = get_object_or_404(Employee, id=request.GET.get("id"))
        context = {
            "emp_id": emp.id,
            "register_number": emp.register_number,
            'languages': Language.objects.all(),
            'education_types': EducationType.objects.all(),
        }
        return render(request, 'operators/3/operator3.html', context)


class Operator3Operator2Empolyees(LoginRequiredMixin, View):

    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator3"):
            raise Http404
        if hasattr(request.user, 'operator3'):
            context = {
                'employees': Employee.objects.filter(step_finished=2, group__id=request.user.operator3.id)
            }
            return render(request, 'operators/3/operator2_employees.html', context)
        else:
            return HttpResponseRedirect("/")


class Operator4(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator4"):
            raise Http404
        emp = get_object_or_404(Employee, id=request.GET.get("id"))
        context = {
            "emp_id": emp.id,
            "register_number": emp.register_number,
            'countries': Country.objects.all()
        }
        return render(request, 'operators/4/operator4.html', context)


class Operator4Operator3Empolyees(LoginRequiredMixin, View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator4"):
            raise Http404
        if hasattr(request.user, 'operator4'):
            context = {
                'employees': Employee.objects.filter(step_finished=3, group__id=request.user.operator4.id),
                'countries': Country.objects.all(),
                # 'employee_countries'
            }
            return render(request, 'operators/4/operator3_employees.html', context)
        else:
            return HttpResponseRedirect("/")


# statistics
class Operator1Stat(View):
    def get(self, request):
        if not hasattr(request.user, "operator") and not hasattr(request.user, "operator1"):
            raise Http404
        qs = Employee.objects.filter(group_id=request.user.operator1.id).values(
            'full_name_en', 'full_name_ru', 'passport_serial', 'passport_given_date', 'passport_expires',
            'passport_image', 'birth_date', 'birth_place', 'lives_at', 'gender', 'inn', 'phone', 'email',
            'register_number'
        )
        context = {
            "employees": qs,
        }
        return render(request, 'operators/1//stat.html', context)
