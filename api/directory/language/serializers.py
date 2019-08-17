from rest_framework.serializers import ModelSerializer

from directory.models import Language


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'id',
            'name_ru',
            'name_en',
            'excellent',
            'good',
            'not_bad',
        ]
