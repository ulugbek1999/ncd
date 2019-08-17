from rest_framework.serializers import ModelSerializer

from directory.models import Country, City, District, Language, EducationType


class CountryCreateSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name_ru',
            'name_en',
            'score'
        )


class CountryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name_ru',
            'name_en',
            'score'
        )


class CityCreateSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = (
            'name_ru',
            'name_en',
            'code'
        )


class CityUpdateSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = (
            'name_ru',
            'name_en',
            'code'
        )


class DistrictCreateSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = (
            'city',
            'name_ru',
            'name_en'
        )


class DistrictUpdateSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = (
            'city',
            'name_ru',
            'name_en'
        )


class LanguageCreateSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'name_ru',
            'name_en',
            'excellent',
            'good',
            'not_bad'
        )


class LanguageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'name_ru',
            'name_en',
            'excellent',
            'good',
            'not_bad'
        )


class EducationTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = EducationType
        fields = (
            'name_ru',
            'name_en',
            'score'
        )


class EducationTypeUpdateSerializer(ModelSerializer):
    class Meta:
        model = EducationType
        fields = (
            'name_ru',
            'name_en',
            'score'
        )
