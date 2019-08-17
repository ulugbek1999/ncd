from django.db.models import Q
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from pure_pagination.mixins import PaginationMixin

from directory.models import City, District
from operators.models import Operator, OperatorGroup
from root.mixins import IsSuperUserMixin


class Operators(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 10
    context_object_name = 'operators'
    template_name = 'root/operators/operators.html'

    def get_queryset(self):
        qs = Operator.objects.all()
        return qs


class OperatorDetail(IsSuperUserMixin, DetailView):
    context_object_name = 'operator'
    template_name = 'root/operators/operator_update.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = Operator.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = OperatorGroup.objects.all()
        return context


class OperatorCreate(IsSuperUserMixin, View):
    template_name = 'root/operators/operator_create.html'

    def get(self, request):
        context = {
            "groups": OperatorGroup.objects.all(),
        }
        return render(request, self.template_name, context)


class OperatorGroups(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 10
    context_object_name = 'groups'
    template_name = 'root/operators/operator_groups.html'

    def get_queryset(self):
        qs = OperatorGroup.objects.all()
        return qs


class OperatorGroupDetail(IsSuperUserMixin, DetailView):
    context_object_name = 'group'
    template_name = 'root/operators/operator_group_update.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = OperatorGroup.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        obj = self.get_queryset().get(id=self.kwargs.get("id"))
        ids = []
        if obj.operator1 is not None:
            ids.append(obj.operator1.id)
        if obj.operator2 is not None:
            ids.append(obj.operator2.id)
        if obj.operator3 is not None:
            ids.append(obj.operator3.id)
        if obj.operator4 is not None:
            ids.append(obj.operator4.id)
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        context["districts"] = District.objects.all()
        context["operators"] = Operator.objects.filter(
            Q(group_operator1=None) |
            Q(group_operator2=None) |
            Q(group_operator3=None) |
            Q(group_operator4=None)
        )
        return context


class OperatorGroupCreate(IsSuperUserMixin, View):
    def get(self, request):
        context = {
            "cities": City.objects.all(),
            "districts": District.objects.all(),
            "operators": Operator.objects.filter(
                Q(group_operator1=None) |
                Q(group_operator2=None) |
                Q(group_operator3=None) |
                Q(group_operator4=None)
            ).order_by('user__username')
        }
        return render(request, "root/operators/operator_group_create.html", context)
