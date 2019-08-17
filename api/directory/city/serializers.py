from rest_framework.serializers import ModelSerializer

from directory.models import City
from api.directory.district.serializers import DistrictSerializer


class CitySerializer(ModelSerializer):
    district = DistrictSerializer(many=True)

    class Meta:
        model = City
        fields = [
            'id',
            'name_ru',
            'name_en',
            'district'
        ]


class CityCreateSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name_ru',
            'name_en',
        ]
