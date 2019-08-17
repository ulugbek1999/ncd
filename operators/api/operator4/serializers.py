from rest_framework.serializers import Serializer
from rest_framework.fields import CharField

from employee.model.employee import Employee


class EmployeeSerializer(Serializer):
    wages = CharField(allow_blank=True)
    is_ready_for_universitet = CharField(allow_blank=True)
    criminal_number = CharField(allow_blank=True)
    criminal_issue = CharField(allow_blank=True)
    criminal_comment_ru = CharField(allow_blank=True)
    add_spec_signs_ru = CharField(allow_blank=True)
    hobby_ru = CharField(allow_blank=True)
    other_ru = CharField(allow_blank=True)
    psycholog = CharField(allow_blank=True)

    def update(self, instance, validated_data):
        if self.context['request'].FILES.get('fingerprint'):
            instance.fingerprint = self.context['request'].FILES.get('fingerprint')
        instance.wages['current'] = validated_data['wages']
        instance.is_ready_for_universitet['current'] = validated_data['is_ready_for_universitet']
        instance.criminal_number['current'] = validated_data['criminal_number']
        instance.criminal_issue['current'] = validated_data['criminal_issue']
        instance.criminal_comment_ru['current'] = validated_data['criminal_comment_ru']
        instance.add_spec_signs_ru['current'] = validated_data['add_spec_signs_ru']
        instance.hobby_ru['current'] = validated_data['hobby_ru']
        instance.other_ru['current'] = validated_data['other_ru']
        instance.psycholog = validated_data['psycholog']
        instance.save()
        return instance
