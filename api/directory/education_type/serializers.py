from rest_framework.serializers import ModelSerializer

from directory.models import EducationType


class EducationTypeSerializer(ModelSerializer):
    class Meta:
        model = EducationType
        fields = [
            'id',
            'name_ru',
            'name_en',
            'score',
        ]
