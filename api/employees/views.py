from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.permissions import IsEmployer
from employee.model.employee import Employee
from .serializers import EmployeeSerializer

class EmployeesList(ListAPIView):
    permission_classes = (IsAuthenticated, IsEmployer, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsEmployer, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "id"
