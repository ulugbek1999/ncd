from django.urls import path

from . import views

urlpatterns = [
    path('operator-1/', views.Employee1.as_view(), name="api.employee.operator1"),
    path('operator-2/<int:id>/', views.Employee2.as_view(), name="employee.operator2"),
    path('operator-3/', views.Employee3.as_view()),
    path('operator:4/<int:id>/', views.Employee4.as_view(), name="api.employee.operator4"),
]
