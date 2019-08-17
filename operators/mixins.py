from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from employee.model.employee import Employee


class GetEmployeeMixin:
    employee = None
    employees = None

    def dispatch(self, request, *args, **kwargs):
        emp_id = request.GET.get('id')
        emp = Employee.objects.filter(id=emp_id)
        if emp.count() == 1:
            self.employee = emp[0]
        try:
            self.employees = Employee.objects.filter(
                group=getattr(request.user.operator, 'group_operator%d' % request.user.operator.operator),
                step_finished=request.user.operator.operator - 1
            )
        except Exception as e:
            print(e)
        return super().dispatch(request, *args, **kwargs)


class IsOperatorMixin:
    """
    check if request.user has attribute `operator`
    Requires LoginRequiredMixen
    """

    def dispatch(self, request, *args, **kwargs):
        print(hasattr(request.user, 'operator'))
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('auth.signin'))
        if not hasattr(request.user, 'operator'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class Operator1Mixin(IsOperatorMixin):
    """checks user is operator or not"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.operator.operator == 1:
            raise PermissionDenied
        if not hasattr(request.user.operator, 'group_operator1'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Operator 2
class Operator2Mixin(IsOperatorMixin, GetEmployeeMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.operator.operator == 2:
            raise PermissionDenied
        if not hasattr(request.user.operator, 'group_operator2'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Operator 3
class Operator3Mixin(IsOperatorMixin, GetEmployeeMixin):
    def dispatch(self, request, *args, **kwargs):
        print(request.user.operator.operator)
        print(request.user.operator.operator not in [3, 4])
        if request.user.operator.operator not in [3, 4]:
            raise PermissionDenied
        if not hasattr(request.user.operator, f'group_operator{request.user.operator.operator}'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Operator 4
class Operator4Mixin(IsOperatorMixin, GetEmployeeMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.operator.operator == 4:
            raise PermissionDenied
        if not hasattr(request.user.operator, 'group_operator4'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
