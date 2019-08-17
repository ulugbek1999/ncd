from rest_framework.generics import CreateAPIView

from employee.model.employee import Employee
from log.models import Log
from .serializers import EmployeeSerializer


class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Log.objects.create(
            operator=self.request.user.operator,
            action='created', employee_id=instance.id
        )
