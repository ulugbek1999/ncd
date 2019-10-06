from django.db.models import Q
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from employee.model.employee import Employee

from employer.models import Employer, EmployerEmployee, EmployerEmployeeRequest
from root.mixins import IsSuperUserMixin


class Employers(IsSuperUserMixin, PaginationMixin, ListView):
    model = Employer
    template_name = "root/employers/employers.html"
    context_object_name = "employers"

    def get_queryset(self):
        qs = Employer.objects.all()
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


class EmployerCreate(IsSuperUserMixin, View):
    template_name = "root/employers/employer_create.html"

    def get(self, request):
        return render(request, self.template_name, {})


class EmployerDetail(IsSuperUserMixin, DetailView):
    context_object_name = 'employer'
    template_name = 'root/employers/employer_update.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs


class EmployersBookmark(IsSuperUserMixin, ListView):
    template_name = 'root/employers/employers_bookmark.html'
    context_object_name = 'employer_requests'

    def get_queryset(self):
        return EmployerEmployeeRequest.objects.all()


class EmployerBookmarks(IsSuperUserMixin, ListView):
    template_name = 'root/employers/employer_bookmarks.html'
    context_object_name = 'employer_requests'

    def get_queryset(self):
        return EmployerEmployeeRequest.objects.filter(id=self.kwargs.get('id'))


class EmployerBookmark(IsSuperUserMixin, DetailView):
    template_name = 'root/employers/employer_bookmark.html'
    context_object_name = 'employee'
    model = Employee
    pk_url_kwarg = 'id'
