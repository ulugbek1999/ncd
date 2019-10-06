from rest_framework.serializers import ModelSerializer

from message_templates.models import Template, TemplateHistory


class MessageTemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = (
            'type',
            'text',
            'title',
        )

class TemplateHistorySerializer(ModelSerializer):
    class Meta:
        model = TemplateHistory
        fields = (
            'title',
            'text',
            'sent_date',
            'message_type',
            'isemployer'
        )