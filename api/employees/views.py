from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsEmployer
from employee.model.employee import Employee
from .serializers import EmployeeSerializer

class EmployeesList(ListAPIView):
    permission_classes = (IsAuthenticated, IsEmployer, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer