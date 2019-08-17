from django.urls import path, include

from operators.api.operator1 import views as op1
from operators.api.operator2 import views as op2
from operators.api.operator3 import views as op3
from operators.api.operator4 import views as op4


operator1_patterns = [
    path('employee/create/', op1.EmployeeCreateAPIView.as_view(), name='api.operator.emplyee.1')
]

operator2_patterns = [
    path('employee/update/<int:id>/', op2.EmployeeUpdateAPIView.as_view(), name='api.operator.emplyee.2')
]

operator3_patterns = [
    path('employee/update/<int:id>/', op3.EmployeeUpdateAPIView.as_view(), name='api.operator.emplyee.3')
]

operator4_patterns = [
    path('employee/update/<int:id>/', op4.EmployeeUpdateAPIView.as_view(), name='api.operator.emplyee.4')
]

urlpatterns = [
    path('op1/', include(operator1_patterns)),
    path('op2/', include(operator2_patterns)),
    path('op3/', include(operator3_patterns)),
    path('op4/', include(operator4_patterns)),
]
