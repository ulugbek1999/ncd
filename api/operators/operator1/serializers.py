from rest_framework.serializers import ModelSerializer

from employee.model.employee import Employee
from log.models import Log


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'full_name_ru',
            'full_name_en',
            'passport_serial',
            'passport_given_date',
            'passport_expires',
            'birth_date',
            'birth_place_ru',
            'living_address_ru',
            'gender',
            'inn',
            'phone',
            'email',
            'register_number',
            'username',
        )

    def create(self, validated_data):
        validated_data['step_finished'] = 1
        request = self.context['request']
        if request.FILES.get('passport_image'):
            validated_data['passport_image'] = request.FILES.get('passport_image')
        if request.POST.get('send_sms'):
            validated_data['send_sms'] = True
        if request.POST.get('send_email'):
            validated_data['send_email'] = True
        validated_data['group'] = request.user.operator.group_operator1
        return super().create(validated_data)
