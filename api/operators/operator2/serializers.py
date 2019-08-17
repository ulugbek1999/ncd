from rest_framework.serializers import ModelSerializer

from employee.model.employee import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'appearance',
            'neatness',
            'skin',
            'height',
            'weight',
            'fatness',
            'blood_group',
            'blood_resus',
            'vision_l',
            'vision_r',
        )

    def update(self, instance, validated_data):
        validated_data['step_finished'] = 2
        request = self.context['request']
        photo_1 = request.FILES.get('photo_1')
        if photo_1:
            validated_data['photo_1'] = photo_1
        photo_2 = request.FILES.get('photo_2')
        if photo_2:
            validated_data['photo_2'] = photo_2
        photo_3 = request.FILES.get('photo_3')
        if photo_3:
            validated_data['photo_3'] = photo_3
        photo_4 = request.FILES.get('photo_4')
        if photo_4:
            validated_data['photo_4'] = photo_4
        return super(EmployeeSerializer, self).update(instance, validated_data)
