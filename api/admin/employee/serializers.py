from rest_framework.serializers import ModelSerializer

from employee.model.employee import Employee


class Employee1Serializer(ModelSerializer):
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
            'birth_place_en',
            'living_address_ru',
            'living_address_en',
            'gender',
            'inn',
            'phone',
            'email',
            'register_number'
        )

    def update(self, instance, validated_data):
        request = self.context['request']
        if request.FILES.get('passport_image'):
            validated_data['passport_image'] = request.FILES.get('passport_image')
        return super().update(instance, validated_data)


class Employee2Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'appearance',
            'neatness',
            'skin',
            'height',
            'weight',
            'fatness',
            'blood_group',
            'blood_resus',
            'vision_l',
            'vision_r',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4'
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class Employee4Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'wages',
            'is_ready_for_university',
            'hobby_ru',
            'other_ru',
            'vision_r',
            'is_employee',
            'is_young_talent',
            'is_student',
            'fingerprint'
        )

    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)


