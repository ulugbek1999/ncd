from django.urls import path

from api.operators.operator2.views import EmployeeCreate

app_name = 'operator2'

urlpatterns = [
    path('employee/create/<int:id>/', EmployeeCreate.as_view(), name='employee.create')
]
