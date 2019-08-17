from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from employee.model.employee import Employee, EmployeeCountry
from log.models import Log
from operators.api.operator4.serializers import EmployeeSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    parser_classes = [FormParser, MultiPartParser]
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        instance = serializer.save()
        c_ids = [j for j in self.request.POST.get('country').split(',')]
        for i in c_ids:
            if i.isdigit():
                _ = EmployeeCountry.objects.create(country_id=i, employee=instance)
        instance.step_finished = 4
        if self.request.POST.get('level'):
            if self.request.POST.get('level') == 'is_employee':
                instance.is_employee = True
            elif self.request.POST.get('level') == 'is_youth_talent':
                instance.is_youth_talent = True
            elif self.request.POST.get('level') == 'is_student':
                instance.is_student = True
        instance.save()
        Log.objects.create(operator=self.request.user.operator, action='created', employee_id=instance.id)
