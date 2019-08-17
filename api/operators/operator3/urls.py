from django.urls import path

from api.operators.operator3.views import EmployeeCreate

app_name = 'operator3'

urlpatterns = [
    path('employee/create/<int:id>/', EmployeeCreate.as_view(), name='employee.create')
]
