from django.urls import path

from api.admin.employee.views import Employee1Update, Employee2Update, Employee4Update, EmployeeDeleteView, \
    EmployeeApplyChanges, EmployeeDeleteChanges, EmployeeChangePasswordAPIView, \
    Employee3OperatorDeleteView

app_name = 'employee'

urlpatterns = [
    path('employee/update/1/<int:id>/', Employee1Update.as_view(), name='1.update'),
    path('employee/update/2/<int:id>/', Employee2Update.as_view(), name='2.update'),
    path('employee/update/4/<int:id>/', Employee4Update.as_view(), name='4.update'),
    path('employee/delete/', EmployeeDeleteView.as_view(), name='delete'),
    path('employee/3operator/delete/', Employee3OperatorDeleteView.as_view(), name='operator_3_delete'),
    path('employee/apply-changes/', EmployeeApplyChanges.as_view(), name='apply-changes'),
    path('employee/delete-changes/', EmployeeDeleteChanges.as_view(), name='delete-changes'),
    path('employee/change-password/<int:emp_id>/', EmployeeChangePasswordAPIView.as_view(), name='change-password'),
]
