from rest_framework.serializers import ModelSerializer

from employee.model.education import Education
from employee.model.army import Army
from employee.model.employee import Employee
from employee.model.relative import Relative
from employee.model.experience import Experience
from employee.model.reward import Reward


class EducationTranslateSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ('name_en', 'address_en', 'specialization_en', 'additional_en')


class ArmyTranslateSerializer(ModelSerializer):
    class Meta:
        model = Army
        fields = ('name_en', 'region_en', 'specialization_en', 'rank_en')


class RelativeTranslateSerializer(ModelSerializer):
    class Meta:
        model = Relative
        fields = ('fullname_en', 'study_work_place_en', 'position_en', 'living_address_en')


class ExperienceTranslateSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ('organization_en', 'position_en', 'sub_division_en', 'address_en')


class RewardTranslateSerializer(ModelSerializer):
    class Meta:
        model = Reward
        fields = ('name_en', 'description_en')


class EmployeeTranslate1Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('birth_place_en', 'living_address_en')


class EmployeeTranslate4Serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('criminal_comment_en', 'add_spec_signs_en', 'hobby_en', 'other_en')

    def update(self, instance, validated_data):
        if self.context['request'].FILES.get('fingerprint'):
            validated_data['fingerprint'] = self.context['request'].FILES.get('fingerprint')
        return super().update(instance, validated_data)
