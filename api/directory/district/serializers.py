from rest_framework.serializers import ModelSerializer

from directory.models import District


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = [
            'id',
            'name_ru',
            'name_en',
        ]
