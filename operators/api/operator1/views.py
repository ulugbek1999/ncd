from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from employee.model.employee import Employee
from log.models import Log
from operators.api.operator1.serializers import EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    parser_classes = [FormParser, MultiPartParser]

    def perform_create(self, serializer):
        # TODO send sms && send email
        instance = serializer.save()
        instance.group = self.request.user.operator1
        instance.step_finished = 1
        instance.save()
        Log.objects.create(operator=self.request.user.operator, action='created', employee_id=instance.id,
                           ip=self.request.META['REMOTE_ADDR'])
