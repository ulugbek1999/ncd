from django.urls import path

from api.operators.operator1.views import EmployeeCreate

app_name = 'operator1'

urlpatterns = [
    path('employee/create/', EmployeeCreate.as_view(), name='employee.create')
]
