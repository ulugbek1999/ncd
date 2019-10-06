from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from employer.models import Employer
from utils.mail import send_email
from utils.sms import send_sms


class EmployerCreateSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = (
            'company_name',
            'phone',
            'email',
            'register_number',
            'boss_fullname',
            'person_fullname_for_hiring',
            'legal_address',
            'workers_amount',
        )

    def create(self, validated_data):
        instance = Employer(**validated_data)
        data = self.context['request'].POST
        if not data.get('username'):
            raise ValidationError({'username': _('Username is missing')})
        if not data.get('password'):
            raise ValidationError({'username': _('Password is missing')})
        if not data.get('password_confirm'):
            raise ValidationError({'username': _('Password confirm is missing')})
        if User.objects.filter(username=data.get('username')).count() > 0:
            raise ValidationError({'username': _('Username already exist')})
        if not data.get('password') == data.get('password_confirm'):
            raise ValidationError({'username': _('Password didnt match')})
        user = User(username=data.get('username'))
        user.save()
        instance.user = user
        instance.save()
        send_email(title='', text=f'Ваш логин на uzncd.com: {data.get("username")}\nВаш пароль: {data.get("password")}', emails=[instance.email, ])
        # send_sms(text=f'your username: {data.get("username")}\nyour password: {data.get("password")}', number=instance.phone)
        return instance
