import datetime
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from rest_framework.fields import IntegerField

from employee.model.employee import Employee
from utils.mail import send_email
from utils.sms import send_sms


class UserSerializer(Serializer):
    employee_id = IntegerField()

    def create(self, validated_data):
        employee = Employee.objects.get(id=validated_data['employee_id'])
        instance = User(username=employee.passport_serial.replace(' ', ''))
        password = datetime.datetime.now().timestamp()
        instance.set_password(password)
        instance.save()
        employee.user = instance
        employee.step_finished = 1
        employee.save()
        if employee.send_sms:
            if employee.phone:
                send_sms(employee.phone, f'Your login on uzncd.com: {instance.username}\nPassword: {password}')
        if employee.send_email:
            if employee.email:
                send_email('Account on uzncd.com', f'Your login on uzncd.com: {instance.username}\nPassword: {password}', [employee.email])
        return validated_data
