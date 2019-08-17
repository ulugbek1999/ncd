from rest_framework.serializers import Serializer
from rest_framework.fields import CharField


class EducationCreateSerializer(Serializer):
    type = CharField()
    name_ru = CharField()
    address_ru = CharField()
    specialization_ru = CharField()
    date_started = CharField()
    date_finished = CharField()
    additional_ru = CharField()

    def update(self, instance, validated_data):
        instance.type_id = validated_data['type']
        instance.name_ru['current'] = validated_data['name_ru']
        instance.address_ru['current'] = validated_data['address_ru']
        instance.specialization_ru['current'] = validated_data['specialization_ru']
        instance.date_started['current'] = validated_data['date_started']
        instance.date_finished['current'] = validated_data['date_finished']
        instance.additional_ru['current'] = validated_data['additional_ru']
        instance.save()
        return instance


class ArmyCreateSerializer(Serializer):
    name_ru = CharField()
    region_ru = CharField()
    specialization_ru = CharField()
    date_started = CharField()
    date_finished = CharField()
    rank_ru = CharField()

    def update(self, instance, validated_data):
        instance.name_ru['current'] = validated_data['name_ru']
        instance.region_ru['current'] = validated_data['region_ru']
        instance.specialization_ru['current'] = validated_data['specialization_ru']
        instance.date_started['current'] = validated_data['date_started']
        instance.date_finished['current'] = validated_data['date_finished']
        instance.rank_ru['current'] = validated_data['rank_ru']
        instance.save()
        return instance


class LanguageCreateSerializer(Serializer):
    level = CharField()

    def update(self, instance, validated_data):
        instance.level['current'] = validated_data['level']
        instance.save()
        return instance


class RelativeCreateSerializer(Serializer):
    level_ru = CharField()
    fullname_ru = CharField()
    birth_date = CharField()
    study_work_place_ru = CharField()
    position_ru = CharField()
    living_address_ru = CharField()

    def update(self, instance, validated_data):
        instance.level_ru['current'] = validated_data['level_ru']
        instance.fullname_ru['current'] = validated_data['fullname_ru']
        instance.birth_date['current'] = validated_data['birth_date']
        instance.study_work_place_ru['current'] = validated_data['study_work_place_ru']
        instance.position_ru['current'] = validated_data['position_ru']
        instance.living_address_ru['current'] = validated_data['living_address_ru']
        instance.save()
        return instance


class RewardCreateSerializer(Serializer):
    name_ru = CharField()
    description_ru = CharField()

    def update(self, instance, validated_data):
        instance.name_ru['current'] = validated_data['name_ru']
        instance.description_ru['current'] = validated_data['description_ru']
        instance.save()
        return instance


class ExperienceCreateSerializer(Serializer):
    organization_ru = CharField()
    date_started = CharField()
    date_finished = CharField()
    position_ru = CharField()
    sub_division_ru = CharField()
    address_ru = CharField()

    def update(self, instance, validated_data):
        instance.organization_ru['current'] = validated_data['organization_ru']
        instance.date_started['current'] = validated_data['date_started']
        instance.date_finished['current'] = validated_data['date_finished']
        instance.position_ru['current'] = validated_data['position_ru']
        instance.sub_division_ru['current'] = validated_data['sub_division_ru']
        instance.address_ru['current'] = validated_data['address_ru']
        instance.save()
        return instance


class FamilyCreateSerializer(Serializer):
    status_ru = CharField()
    children_amount = CharField()

    def update(self, instance, validated_data):
        instance.status_ru['current'] = validated_data['status_ru']
        instance.children_amount['current'] = validated_data['children_amount']
        instance.save()
        return instance
