from rest_framework.serializers import ModelSerializer

from employee.model.employee import Employee


# new
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'full_name_en',
            'full_name_ru',
            'passport_serial',
            'passport_given_date',
            'passport_expires',
            'passport_image',
            'birth_date',
            'birth_place_ru',
            'lives_at_ru',
            'gender',
            'inn',
            'phone',
            'email',
            'register_number',
        ]

    def create(self, validated_data):
        validated_data['step_finished'] = 1
        return super(EmployeeSerializer, self).create(validated_data)
