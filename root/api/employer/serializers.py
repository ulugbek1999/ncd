from rest_framework.serializers import Serializer
from rest_framework.serializers import CharField


class CreateSerializer(Serializer):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    middle_name = CharField(max_length=255)
    username = CharField(max_length=255)
    phone = CharField(max_length=255)
    company_name = CharField(max_length=255)
