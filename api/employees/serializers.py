from rest_framework.serializers import ModelSerializer, StringRelatedField
from employee.model.employee import Employee, EmployeeCountry
from employee.model.army import Army, ArmyFile
from employee.model.education import Education, EducationFile
from directory.models import EducationType
from employee.model.experience import Experience, ExperienceFile
from employee.model.family import Family, FamilyFile
from employee.model.language import Language, LanguageFile
from employee.model.reward import Reward, RewardFile
from directory.models import Country


class RewardFileSerializer(ModelSerializer):
    class Meta:
        model = RewardFile
        fields = ("file", )

class RewardSerializer(ModelSerializer):
    rew_file = RewardFileSerializer(many=True, read_only=True)

    class Meta:
        model = Reward
        fields = (
            "name_ru",
            "name_en",
            "description_ru",
            "description_en",
            "rew_file",
        )

class LanguageFileSerializer(ModelSerializer):
    class Meta:
        model = LanguageFile
        fields = ("file", )

class LanguageSerializer(ModelSerializer):
    lang_file = LanguageFileSerializer(many=True, read_only=True)

    class Meta:
        model = Language
        fields = (
            "language",
            "level",
            "lang_file"
        )

class FamilyFileSerializer(ModelSerializer):
    class Meta:
        model = FamilyFile
        fields = ("file", )

class FamilySerializer(ModelSerializer):
    fam_file = FamilyFileSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = (
            "status",
            "children_amount",
            "fam_file"
        )

class ExperienceFileSerializer(ModelSerializer):
    class Meta:
        model = ExperienceFile
        fields = ("file", )

class ExperienceSerializer(ModelSerializer):
    exp_file = ExperienceFileSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = (
            "organization_ru",
            "organization_en",
            "date_started",
            "date_finished",
            "position_ru",
            "position_en",
            "sub_division_ru",
            "sub_division_en",
            "address_ru",
            "address_en",
            "exp_file"
        )

class ArmyFileSerializer(ModelSerializer):
    class Meta:
        model = ArmyFile
        fields = ("file", )

class ArmySerializer(ModelSerializer):
    army_file = ArmyFileSerializer(many=True, read_only=True)
    class Meta:
        model = Army
        fields = (
            "name_ru",
            "name_en",
            "region_ru",
            "region_en",
            "specialization_ru",
            "specialization_en",
            "date_started",
            "date_finished",
            "rank_ru",
            "rank_en",
            "army_file",
        )

class EducationFileSerializer(ModelSerializer):
    class Meta:
        model = EducationFile
        fields = ("file", )

class EducationTypeSerializer(ModelSerializer):
    class Meta:
        model = EducationType
        fields = ("name_ru", "name_en", )

class EducationSerializer(ModelSerializer):
    edu_file = EducationFileSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = (
            "type",
            "name_ru",
            "name_en",
            "address_ru",
            "address_en",
            "specialization_ru",
            "specialization_en",
            "date_started",
            "date_finished",
            "additional_ru",
            "additional_en",
            "edu_file",
        )



class EmployeeCountriesSerializer(ModelSerializer):
    class Meta:
        model = EmployeeCountry
        fields = ("country_id", )

class EmployeeSerializer(ModelSerializer):
    army = ArmySerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    experience = ExperienceSerializer(many=True, read_only=True)
    family = FamilySerializer(many=False, read_only=True)
    reward = RewardSerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)
    countries = EmployeeCountriesSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            "id",
            "full_name_ru",
            "full_name_en",
            "passport_serial",
            "passport_given_date",
            "passport_expires",
            "passport_image",
            "birth_date",
            "birth_place_ru",
            "birth_place_en",
            "living_address_ru",
            "living_address_en",
            "gender",
            "inn",
            "phone",
            "email",
            "register_number",
            "appearance",
            "neatness",
            "skin",
            "height",
            "weight",
            "fatness",
            "blood_group",
            "blood_resus",
            "vision_l",
            "vision_r",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "military_duty",
            "wages",
            "is_ready_for_university",
            "hobby_ru",
            "hobby_en",
            "other_ru",
            "other_en",
            "education",
            "army",
            "family",
            "experience",
            "reward",
            "language",
            "countries",
        )