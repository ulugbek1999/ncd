from django.urls import path

from api.admin.employer.views import EmployerCreateAPIView, EmployerDeleteAPIView, \
    EmployerCreateAccountAPIView, EmployerEmployeeMakeBusy, EmployerRequestDeleteAPIView,\
    EmployersRequestDeleteAPIView

app_name = 'employer'

urlpatterns = [
    path('create/', EmployerCreateAPIView.as_view(), name='create'),
    path('change-account/<int:employer_id>', EmployerCreateAccountAPIView.as_view(), name='change-account'),
    path('delete/', EmployerDeleteAPIView.as_view(), name='delete'),
    path('employer-employee-request/delete/', EmployerRequestDeleteAPIView.as_view(), name='employer-employee-request-delete'),
    path('employee/make-busy/', EmployerEmployeeMakeBusy.as_view(), name='employee-make-busy'),
    path('request/delete/', EmployersRequestDeleteAPIView.as_view(), name='request-delete'),
]
