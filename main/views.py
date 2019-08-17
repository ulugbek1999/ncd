"""
TODO Permission denied page qilish kk
"""

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import render


class Index(LoginRequiredMixin, View):
    def get(self, request):
        if hasattr(request.user, 'operator'):
            if hasattr(request.user.operator, 'group_operator1'):
                return HttpResponseRedirect(reverse("operator:1"))
            elif hasattr(request.user.operator, 'group_operator2'):
                return HttpResponseRedirect(reverse("operator:2"))
            elif hasattr(request.user.operator, 'group_operator3'):
                return HttpResponseRedirect(reverse("operator:3"))
            elif hasattr(request.user.operator, 'group_operator4'):
                return HttpResponseRedirect(reverse("operator:4"))
            else:
                raise PermissionDenied
        elif request.user.is_superuser:
            return HttpResponseRedirect(reverse("root.employee.list"))
        else:
            raise PermissionDenied


class AuthSignin(View):
    def get(self, request):
        return render(request, 'auth/signin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'auth/signin.html', {'error': True})


class AuthSignout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
