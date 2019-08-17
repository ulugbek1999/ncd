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
        )

    def update(self, instance, validated_data):
        request = self.context['request']
        photo_1 = request.FILES.get('photo_1')
        if photo_1:
            validated_data['photo_1'] = photo_1
        photo_2 = request.FILES.get('photo_2')
        if photo_2:
            validated_data['photo_2'] = photo_2
        photo_3 = request.FILES.get('photo_3')
        if photo_3:
            validated_data['photo_3'] = photo_3
        photo_4 = request.FILES.get('photo_4')
        if photo_4:
            validated_data['photo_4'] = photo_4
        return super().update(instance, validated_data)


class Employee4Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'wages',
            'is_ready_for_university',
            'criminal_number',
            'criminal_issue',
            'criminal_comment_ru',
            'add_spec_signs_ru',
            'hobby_ru',
            'other_ru',
            'psycholog',
            'vision_r',
        )

    def update(self, instance, validated_data):
        request = self.context['request']
        if request.POST.get('level'):
            if request.POST.get('level') == 'is_employee':
                validated_data['is_employee'] = True
            elif request.POST.get('level') == 'is_youth_talent':
                validated_data['is_youth_talent'] = True
            elif request.POST.get('level') == 'is_student':
                validated_data['is_student'] = True
        fingerprint = request.FILES.get('fingerprint')
        if fingerprint:
            validated_data['fingerprint'] = fingerprint
        return super().update(instance, validated_data)


