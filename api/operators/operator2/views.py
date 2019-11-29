from rest_framework.generics import UpdateAPIView

from employee.model.employee import Employee
from log.models import Log
from .serializers import EmployeeSerializer
from rest_framework.response import Response


class EmployeeCreate(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Log.objects.create(
            operator=self.request.user.operator,
            action='created', employee_id=instance.id
        )

