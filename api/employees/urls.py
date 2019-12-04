from django.urls import path
from .views import EmployeesList

urlpatterns = [
    path("list", EmployeesList.as_view())
]
