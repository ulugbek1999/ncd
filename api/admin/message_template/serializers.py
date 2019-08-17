from rest_framework.serializers import ModelSerializer

from message_templates.models import Template


class MessageTemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = (
            'type',
            'text',
            'title',
        )
