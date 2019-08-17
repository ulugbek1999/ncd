from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from employee.model.employee import Employee
from log.models import Log
from operators.api.operator2.serializers import EmployeeSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    parser_classes = [FormParser, MultiPartParser]
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.step_finished = 2
        instance.save()
        Log.objects.create(operator=self.request.user.operator, action='created', employee_id=instance.id,
                           ip=self.request.META['REMOTE_ADDR'])
