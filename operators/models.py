import datetime
import calendar
import hashlib
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import Q

from directory.models import District


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='operator')
    phone = models.CharField(max_length=50, blank=True, default='')
    operator = models.IntegerField(default=0, blank=True)
    channel = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        db_table = 'operator'
        ordering = ['-id',]

    def __str__(self):
        return self.user.username

    @property
    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def has_channel(self):
        return not self.channel == ''

    @property
    def has_phone(self):
        return not self.phone == ''

    @property
    def has_group(self):
        if hasattr(self, 'group_operator1'):
            return True
        elif hasattr(self, 'group_operator2'):
            return True
        elif hasattr(self, 'group_operator3'):
            return True
        elif hasattr(self, 'group_operator4'):
            return True
        return False

    @property
    def group(self):
        if getattr(self, 'group_operator%d' % self.operator):
            return getattr(self, 'group_operator%d' % self.operator)

    @property
    def get_register_number(self):
        today = datetime.datetime.today()
        year = str(today.year)[-1]
        month = str(today.month); month = f"0{month}" if len(month) == 1 else month
        weekday = ["A", "B", "C", "D", "E", "F", "G"][today.isoweekday()-1]
        day = f"0{today.day}" if len(str(today.day)) == 1 else today.day
        card_number = RegisterNumber.objects.get_or_create(id=1)
        if card_number[0].number == 0:
            card_number[0].number = 1
            card_number[0].save()
        if card_number[0].number < 10:
            card_number[0].number = f"00{card_number[0].number}"
        elif card_number[0].number < 100:
            card_number[0].number = f"0{card_number[0].number}"
        else:
            card_number[0].number = str(card_number[0].number)
        return f"{year}{month}{weekday}-{day}{card_number[0].number}{self.user.operator.group_operator1.district.city.code}"


class OperatorGroup(models.Model):
    group_name = models.CharField(max_length=255, default='', blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    operator1 = models.OneToOneField(Operator, on_delete=models.SET_NULL, related_name='group_operator1', null=True, blank=True)
    operator2 = models.OneToOneField(Operator, on_delete=models.SET_NULL, related_name='group_operator2', null=True, blank=True)
    operator3 = models.OneToOneField(Operator, on_delete=models.SET_NULL, related_name='group_operator3', null=True, blank=True)
    operator4 = models.OneToOneField(Operator, on_delete=models.SET_NULL, related_name='group_operator4', null=True, blank=True)

    class Meta:
        db_table = 'operator_group'
        ordering = ['-id',]

    def __str__(self):
        return f'{self.group_name}'


@receiver(post_save, sender=Operator)
def generate_channel_name(instance, created, **kwargs):
    if created:
        if not instance.has_channel:
            i_full_name = str(instance.fullname).encode()
            i_id = str(instance.id).encode()
            channel = hashlib.md5(i_full_name+i_id)
            instance.channel = channel.hexdigest()
            instance.save()


class RegisterNumber(models.Model):
    number = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = "operator_register_number"

    def __str__(self):
        return f"{self.number}"
