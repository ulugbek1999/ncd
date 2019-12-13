from django.urls import path
from .views import EmployeesList, EmployeeRetrieveAPIView

urlpatterns = [
    path("list", EmployeesList.as_view()),
    path("<int:id>", EmployeeRetrieveAPIView.as_view())
]
