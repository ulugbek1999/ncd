from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_206_PARTIAL_CONTENT
from rest_framework.response import Response
from utils.permissions import IsEmployer
from employee.model.employee import Employee
from .serializers import EmployeeSerializer
from employer.models import EmployerEmployeeRequest

class EmployeesList(ListAPIView):
    permission_classes = (IsAuthenticated, IsEmployer, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(APIView):
    permission_classes = (IsAuthenticated, IsEmployer, )

    def get(self, request, id):
        try:
            employee = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response("Employee not found!", status=HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        employer_request = EmployerEmployeeRequest.objects.filter(employer=request.user.employer)
        if employer_request.count() == 1:
            try:
                employer_request[0].employees.get(pk=id)
            except Employee.DoesNotExist:
                return Response(serializer.data, status=HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serializer.data, status=HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.data, status=HTTP_200_OK)

class EmployeeRequestList(APIView):
    permission_classes = (IsAuthenticated, IsEmployer, )

    def get(self, request):
        employees = EmployerEmployeeRequest.objects.filter(employer=request.user.employer)[0].employees
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=HTTP_200_OK)