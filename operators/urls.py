from django.urls import path, include

from .views.operator1 import Operator1, Operator1Stat
from .views.operator2 import Operator2, Operator2Operator1Empolyees
from .views.operator3 import Operator3, Operator3Operator2Empolyees
from .views.operator4 import Operator4, Operator4Operator3Empolyees, EmployeeUpdateOP3

app_name = 'operator'

urlpatterns = [
    path('1/', Operator1.as_view(), name='1'),
    path('2/', Operator2.as_view(), name='2'),
    path('3/', Operator3.as_view(), name='3'),
    path('4/', Operator4.as_view(), name='4'),
    path('2/1op/', Operator2Operator1Empolyees.as_view(), name='2.employees'),
    path('3/2op/', Operator3Operator2Empolyees.as_view(), name='3.employees'),
    path('4/3op/', Operator4Operator3Empolyees.as_view(), name='4.employees'),
    path('4/3op/view/<int:id>/', EmployeeUpdateOP3.as_view(), name='4.3.update'),

    path('1/stat/', Operator1Stat.as_view(), name='1.stat'),

    # path('api/', include('operators.api.urls'))
]
