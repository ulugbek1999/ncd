from rest_framework.permissions import BasePermission
from employer.models import Employer
from django.contrib.auth.models import User

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "employer")

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "employee")
