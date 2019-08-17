from django.db.models import Q
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from employee.model.employee import Employee

from partner.models import Partner, PartnerEmployee, PartnerEmployeeRequest
from root.mixins import IsSuperUserMixin


class Partners(IsSuperUserMixin, PaginationMixin, ListView):
    model = Partner
    template_name = "root/partners/partners.html"
    context_object_name = "partners"

    def get_queryset(self):
        qs = Partner.objects.all()
        username = self.request.GET.get('username')
        if username:
            qs = qs.filter(user__username__icontains=username)
        fullname = self.request.GET.get('fullname')
        if fullname:
            qs = qs.filter(
                Q(boss_fullname__icontains=fullname) |
                Q(person_fullname_for_hiring__icontains=fullname)
            )
        phone = self.request.GET.get('phone')
        if phone:
            qs = qs.filter(phone__icontains=phone)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('username')
        if username:
            context['username'] = username
        fullname = self.request.GET.get('fullname')
        if fullname:
            context['fullname'] = fullname
        phone = self.request.GET.get('phone')
        if phone:
            context['phone'] = phone
        return context


class PartnerCreate(IsSuperUserMixin, View):
    template_name = "root/partners/partner_create.html"

    def get(self, request):
        return render(request, self.template_name, {})


class PartnerDetail(IsSuperUserMixin, DetailView):
    context_object_name = 'partner'
    template_name = 'root/partners/partner_update.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = Partner.objects.all()
        return qs


class PartnersBookmark(IsSuperUserMixin, ListView):
    template_name = 'root/partners/partners_bookmark.html'
    context_object_name = 'partner_requests'

    def get_queryset(self):
        return PartnerEmployeeRequest.objects.all()


class PartnerBookmarks(IsSuperUserMixin, ListView):
    template_name = 'root/partners/partner_bookmarks.html'
    context_object_name = 'partner_requests'

    def get_queryset(self):
        return PartnerEmployeeRequest.objects.filter(id=self.kwargs.get('id'))


class PartnerBookmark(IsSuperUserMixin, DetailView):
    template_name = 'root/partners/partner_bookmark.html'
    context_object_name = 'employee'
    model = Employee
    pk_url_kwarg = 'id'
