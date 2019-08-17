from rest_framework.serializers import ModelSerializer

from employee.model.employee import Employee, EmployeeCountry


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'wages',
            'is_ready_for_university',
            'criminal_number',
            'criminal_issue',
            'criminal_comment_ru',
            'add_spec_signs_ru',
            'hobby_ru',
            'other_ru',
            'psycholog',
            'vision_r',
        )

    def update(self, instance, validated_data):
        request = self.context['request']
        validated_data['step_finished'] = 4

        c_ids = [j for j in request.POST.get('country').split(',')]
        for i in c_ids:
            if i.isdigit():
                _ = EmployeeCountry.objects.create(country_id=i, employee=instance)
        if request.POST.get('level'):
            if request.POST.get('level') == 'is_employee':
                validated_data['is_employee'] = True
            elif request.POST.get('level') == 'is_youth_talent':
                validated_data['is_youth_talent'] = True
            elif request.POST.get('level') == 'is_student':
                validated_data['is_student'] = True
        fingerprint = request.FILES.get('fingerprint')
        if fingerprint:
            validated_data['fingerprint'] = fingerprint
        return super(EmployeeSerializer, self).update(instance, validated_data)
