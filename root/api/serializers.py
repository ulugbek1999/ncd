from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.fields import CharField

from employee.model.employee import Employee
from operators.models import OperatorGroup, Operator
from employer.models import Employer


class AdminEmployeeUpdate1Serializer(ModelSerializer):

    full_name_en = CharField(allow_blank=True)
    full_name_ru = CharField(allow_blank=True)
    passport_serial = CharField(allow_blank=True)
    passport_given_date = CharField(allow_blank=True)
    passport_expires = CharField(allow_blank=True)
    # birth_date = CharField(allow_blank=True)
    birth_place_ru = CharField(allow_blank=True)
    lives_at_ru = CharField(allow_blank=True)
    gender = CharField(allow_blank=True)
    inn = CharField(allow_blank=True)
    phone = CharField(allow_blank=True)
    email = CharField(allow_blank=True)


class AdminEmployeeUpdate2Serializer(ModelSerializer):

    appearance = CharField(allow_blank=True)
    neatness = CharField(allow_blank=True)
    skin = CharField(allow_blank=True)
    height = CharField(allow_blank=True)
    weight = CharField(allow_blank=True)
    fatness = CharField(allow_blank=True)
    blood_group = CharField(allow_blank=True)
    blood_resus = CharField(allow_blank=True)
    vision_l = CharField(allow_blank=True)
    vision_r = CharField(allow_blank=True)


class AdminEmployeeUpdate4Serializer(ModelSerializer):
    wages = CharField(allow_blank=True)
    is_ready_for_universitet = CharField(allow_blank=True)
    criminal_number = CharField(allow_blank=True)
    criminal_issue = CharField(allow_blank=True)
    criminal_comment_ru = CharField(allow_blank=True)
    add_spec_signs_ru = CharField(allow_blank=True)
    hobby_ru = CharField(allow_blank=True)
    other_ru = CharField(allow_blank=True)
    psycholog = CharField(allow_blank=True)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = OperatorGroup
        fields = [
            "group_name", "district", "operator1",
            "operator2", "operator3", "operator4"
        ]


class OperatorSerializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = [
            "phone", "operator"
        ]


# Employer
class EmployerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            'company_name',
            'phone',
            'register_number',
            'boss_fullname',
            'person_fullname_for_hiring',
            'legal_address',
            'workers_amount',
        ]


# Employee Translations
class EmployeeTranslationSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['birth_place_en', 'living_address_en']
