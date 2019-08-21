from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin

from directory.models import City
from employee.model.employee import Employee
from message_templates.models import Template, TemplateHistory, PartnerTemplateHistory, EmployeeTemplateHistory
from partner.models import Partner
from root.mixins import IsSuperUserMixin
from django.template.defaulttags import register


class TemplateList(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 12
    model = Template
    template_name = 'root/templates/list.html'
    context_object_name = 'templates'

class TemplateHistoryList(IsSuperUserMixin, PaginationMixin, ListView):
    paginate_by = 12
    model = TemplateHistory
    template_name = 'root/templates/history.html'
    context_object_name = 'histories'

    @register.filter
    def shortify_text_length(value):
        if len(value) > 80:
            return value[:80] + "..."
        return value
    
    @register.filter
    def shortify_title_length(value):
        if len(value) > 15:
            return value[:15] + "..."
        return value

class TemplateHistoryDetailView(IsSuperUserMixin, DetailView):
    template_name = 'root/templates/history_detail.html'
    context_object_name = 'template_history'
    pk_url_kwarg = 'id'
    model = TemplateHistory

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    def get_context_data(self, *args, **kwargs):
        history_template_id = self.kwargs["id"]
        data = {}
        context = super().get_context_data(**kwargs)
        ids = []
        if self.object.ispartner == False:
            qs = EmployeeTemplateHistory.objects.filter(template_history_id__exact=history_template_id)
            for q in qs:
                ids.append(q.employee_id)
            employees = Employee.objects.filter(id__in=ids)
            context["employees"] = employees    
                # context["employees"] = employee
        else:
            qs = PartnerTemplateHistory.objects.filter(template_history_id__exact=history_template_id)
            for q in qs:
                ids.append(q.partner_id)
            partner = Partner.objects.filter(id__in=ids)
            context["partners"] = partner
        return context



class TemplateDetailView(IsSuperUserMixin, DetailView):
    template_name = 'root/templates/detail.html'
    context_object_name = 'template'
    pk_url_kwarg = 'id'
    model = Template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request)
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
