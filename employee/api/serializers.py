from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from employee.model.employee import Employee


class EmployeeStep1Serializer(ModelSerializer):
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


class EmployeeStep2Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "appearance", "neatness", "skin", "height",
            "weight", "fatness", "blood_group", "blood_resus",
            "vision_l", "vision_r",
            "photo_1", "photo_2", "photo_3", "photo_4"
        ]


class EmployeeStep3EducationSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'type', 'name_ru', 'address_ru', 'specialization_ru',
            'date_started', 'date_finished', 'additional_ru',
        ]


class EmployeeCountry(Serializer):
    country = serializers.CharField()


class EmployeeStep4Serializer(ModelSerializer):
    # country = EmployeeCountry(many=True)

    class Meta:
        model = Employee
        fields = [
            "wages", "is_ready_for_university", "criminal_number",
            "criminal_issue", "criminal_comment_ru", "add_spec_signs_ru", "hobby_ru",
            "other_ru", "psycholog"
        ]
    
    def update(self, instance, validated_data):
        print(validated_data)
        return super(EmployeeStep4Serializer, self).update(instance, validated_data)
