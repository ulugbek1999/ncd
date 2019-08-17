from django.urls import path

from api.operators.operator4.views import EmployeeCreate

app_name = 'operator4'

urlpatterns = [
    path('employee/create/<int:id>/', EmployeeCreate.as_view(), name='employee.create')
]
