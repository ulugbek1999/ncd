from django.urls import path
from .views import EmployeesList, EmployeeRetrieveAPIView
from .views import EmployeeRequestList

urlpatterns = [
    path("list", EmployeesList.as_view()),
    path("<int:id>", EmployeeRetrieveAPIView.as_view()),
    path("employer-list", EmployeeRequestList.as_view())
]
