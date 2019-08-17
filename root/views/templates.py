from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin

from directory.models import City
from employee.model.employee import Employee
from message_templates.models import Template, TemplateHistory
from partner.models import Partner
from root.mixins import IsSuperUserMixin


class TemplateList(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 12
    model = Template
    template_name = 'root/templates/list.html'
    context_object_name = 'templates'

class TemplateHistoryList(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 12
    model = TemplateHistory
    template_name = 'root/templates/history.html'
    context_object_name = 'history'


class TemplateDetailView(IsSuperUserMixin, DetailView):
    template_name = 'root/templates/detail.html'
    context_object_name = 'template'
    pk_url_kwarg = 'id'
    model = Template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.type == 1:
            self.template_name = 'root/templates/employees.html'
            qs = Employee.objects.all()
            context['employees'] = Employee.objects.search_filter(qs, self.request)
        elif self.object.type == 2:
            self.template_name = 'root/templates/partners.html'
            qs = Partner.objects.filter(user__isnull=False)
            context['partners'] = Partner.objects.search_filter(qs, self.request)
        context['cities'] = City.objects.all()
        for k, v in self.request.GET.items():
            context[k] = v
        return context
