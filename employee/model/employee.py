import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _, get_language

from employee.file_handlers import fingerprint, passport_copy, photos
from directory.models import Country
from operators.models import OperatorGroup
from utils.mail import send_email
from utils.sms import send_sms


class EmployeeManager(models.Manager):
    def search_filter(self, qs, request):
        """
        :param qs: Employee objects
        :param request: request
        :return: queryset of Employee
        """
        if request.GET.get('fullname'):
            fullname = request.GET.get('fullname')
            qs = qs.filter(
                Q(full_name_ru__icontains=fullname) |
                Q(full_name_en__icontains=fullname)
            )
        if request.GET.get('gender'):
            gender = request.GET.get('gender')
            qs = qs.filter(gender=gender)
        if request.GET.get('phone'):
            phone = request.GET.get('phone')
            qs = qs.filter(phone__icontains=phone)
        if request.GET.get('category'):
            category = request.GET.get('category')
            qs = qs.filter(score__category=category)
        return qs


GENDER = (
    ("m", _('Male')),
    ("f", _('Female')),
)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('User'))
    step_finished = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Step finished'))
    group = models.ForeignKey(OperatorGroup, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Group'))
    created = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name=_('Created'))
    updated = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name=_('Updated'))
    send_sms = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('I must send SMS'))
    send_email = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('I must send Email'))
    op2_ws_sent = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Notification sent to Operator 2'))
    op3_ws_sent = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Notification sent to Operator 3'))
    op4_ws_sent = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Notification sent to Operator 4'))

    full_name_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Fullname ru'))
    full_name_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Fullname en'))
    passport_serial = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Passport serial'))
    passport_given_date = models.DateField(null=True, blank=True,  verbose_name=_('Passport given date'))
    passport_expires = models.DateField(null=True, blank=True,  verbose_name=_('Passport expires'))
    passport_image = models.ImageField(default="default/default.jpg",  upload_to=passport_copy, verbose_name=_('Passport image'))
    birth_date = models.DateField(blank=True,  null=True, verbose_name=_('Birth date'))
    birth_place_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Birth place ru'))
    birth_place_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Birth place en'))
    living_address_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Living address ru'))
    living_address_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Living address en'))
    gender = models.CharField(max_length=1, default='m', blank=True, null=True, choices=GENDER, verbose_name=_('Gender'))
    inn = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Inn'))
    phone = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Phone'))
    email = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Email'))
    register_number = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Register number'))

    appearance = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Appearance'))
    neatness = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Neatness'))
    skin = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Skin'))
    height = models.FloatField(default=0, blank=True, null=True, verbose_name=_('Height'))
    weight = models.FloatField(default=0, blank=True, null=True, verbose_name=_('Weight'))
    fatness = models.FloatField(default=0, blank=True, null=True, verbose_name=_('Fatness'))
    blood_group = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Blood group'))
    blood_resus = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Blood resus'))
    vision_l = models.FloatField(default=0, blank=True, null=True, verbose_name=_('Vision left'))
    vision_r = models.FloatField(default=0, blank=True, null=True, verbose_name=_('Vision right'))
    photo_1 = models.ImageField(blank=True, null=True, upload_to=photos, verbose_name=_('Photo1'))
    photo_2 = models.ImageField(blank=True, null=True, upload_to=photos, verbose_name=_('Photo2'))
    photo_3 = models.ImageField(blank=True, null=True, upload_to=photos, verbose_name=_('Photo3'))
    photo_4 = models.ImageField(blank=True, null=True, upload_to=photos, verbose_name=_('Photo4'))

    military_duty = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Military duty'))

    wages = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Wages'))
    is_ready_for_university = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Ready for university'))
    criminal_number = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Criminal number'))
    criminal_issue = models.DateField(null=True, blank=True, verbose_name=_('Criminal issue'))
    criminal_comment_ru = models.TextField(default='', blank=True, null=True, verbose_name=_('Criminal comment ru'))
    criminal_comment_en = models.TextField(default='', blank=True, null=True, verbose_name=_('Criminal comment en'))
    add_spec_signs_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Spec signs ru'))
    add_spec_signs_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Spec signs en'))
    hobby_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Hobby ru'))
    hobby_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Hobby en'))
    other_ru = models.TextField(default='', blank=True, null=True, verbose_name=_('Other ru'))
    other_en = models.TextField(default='', blank=True, null=True, verbose_name=_('Other en'))
    psycholog = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Psycholog'))
    fingerprint = models.ImageField(upload_to=fingerprint, blank=True, null=True, verbose_name=_('Fingerprint'))

    busy = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Busy'))
    is_student = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Student'))
    is_young_talent = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Young talent'))
    is_employee = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Employee'))
    can_change = models.BooleanField(default=False, blank=True, null=True, verbose_name=_('Can change profile'))
    is_sent_to_check = models.BooleanField(default=False, blank=True, null=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    objects = EmployeeManager()

    class Meta:
        db_table = 'employee'
        ordering = ("-id",)
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.full_name_ru

    @property
    def full_name(self) -> str:
        if get_language() == 'ru':
            return self.full_name_ru
        elif get_language() == 'en':
            return self.full_name_en
        return self.full_name_ru

    @property
    def birth_place(self) -> str:
        if get_language() == 'ru':
            return self.birth_place_ru
        elif get_language() == 'en':
            return self.birth_place_en
        return self.birth_place_ru

    @property
    def living_address(self) -> str:
        if get_language() == 'ru':
            return self.living_address_ru
        elif get_language() == 'en':
            return self.living_address_en
        return self.living_address_ru

    @property
    def criminal_comment(self) -> str:
        if get_language() == 'ru':
            return self.criminal_comment_ru
        elif get_language() == 'en':
            return self.criminal_comment_en
        return self.criminal_comment_ru

    @property
    def add_spec_signs(self) -> str:
        if get_language() == 'ru':
            return self.add_spec_signs_ru
        elif get_language() == 'en':
            return self.add_spec_signs_en
        return self.add_spec_signs_ru

    @property
    def hobby(self) -> str:
        if get_language() == 'ru':
            return self.hobby_ru
        elif get_language() == 'en':
            return self.hobby_en
        return self.hobby_ru

    @property
    def other(self) -> str:
        if get_language() == 'ru':
            return self.other_ru
        elif get_language() == 'en':
            return self.other_en
        return self.other_ru

    @property
    def has_family(self):
        return hasattr(self, 'family')

    @property
    def get_gender_display(self):
        return _('Male') if self.gender == "m" else _('Female')

    @property
    def get_is_ready_for_universitet_display(self):
        return _('Yes') if self.is_ready_for_university else _('No')

    @property
    def age(self):
        if self.birth_date:
            return datetime.datetime.today().year - self.birth_date.year
        return 0

    def medical_score(self):
        total = 0
        if self.gender == "m":
            if 150 <= self.height < 165:
                total += 1
            elif 165 <= self.height < 170:
                total += 2
            elif 170 <= self.height < 175:
                total += 4
            elif 175 <= self.height < 180:
                total += 8
            elif 180 <= self.height:
                total += 10
            if 45 <= self.weight < 55:
                total += 1
            elif 55 <= self.weight < 65:
                total += 4
            elif 65 <= self.weight < 75:
                total += 8
            elif 75 <= self.weight < 85:
                total += 10
            elif 85 <= self.weight < 95:
                total += 8
            elif 95 <= self.weight:
                total += 4
        elif self.gender == "f":
            if 150 <= self.height < 165:
                total += 2
            elif 165 <= self.height < 170:
                total += 4
            elif 170 <= self.height < 175:
                total += 8
            elif 175 <= self.height < 180:
                total += 10
            elif 180 <= self.height:
                total += 6
            if 45 <= self.weight < 55:
                total += 4
            elif 55 <= self.weight < 65:
                total += 8
            elif 65 <= self.weight < 75:
                total += 10
            elif 75 <= self.weight < 85:
                total += 6
            elif 85 <= self.weight < 95:
                total += 4
            elif 95 <= self.weight:
                total += 2
        if self.vision_l or self.vision_r == 1.2:
            total += 10
        if 0.8 <= self.vision_l or self.vision_r <= 1:
            total += 8
        if 0.5 <= self.vision_l or self.vision_r < 0.8:
            total += 6
        if 0.1 <= self.vision_l or self.vision_r <= 0.4:
            total += 4
        return total

    def birth_date_score(self):
        if self.birth_date is None:
            return 0
        if 2000 >= int(self.birth_date.year) > 1998:
            return 4
        if 1998 >= int(self.birth_date.year) > 1990:
            return 10
        if 1990 >= int(self.birth_date.year) > 1986:
            return 8
        if 1986 >= int(self.birth_date.year) > 1982:
            return 6
        if 1982 >= int(self.birth_date.year) > 1978:
            return 4
        return 0

    def university_score(self):
        if self.is_ready_for_university:
            return 10
        else:
            if self.age < 30:
                return 2
            elif self.age < 35:
                return 4
            elif 35 <= self.age < 40:
                return 6
        return 0

    def wages_score(self) -> int:
        if self.wages == '500-1000':
            return 10
        elif self.wages == '1000-1500':
            return 8
        elif self.wages == '1500-2000':
            return 6
        elif self.wages == '2500':
            return 4
        return 0

    def get_countries_list(self):
        if get_language() == 'ru':
            return ', '.join(i.country.name_ru for i in self.countries.all())
        elif get_language() == 'en':
            return ', '.join(i.country.name_en for i in self.countries.all())
        elif get_language() == 'uz':
            return ', '.join(i.country.name_ru for i in self.countries.all())

    @staticmethod
    def send_sms_message(ids, title, text):
        # TODO strip &nbsp; tags
        employees = Employee.objects.filter(id__in=ids)
        for e in employees:
            if e.phone:
                send_sms(e.phone, title + '\n' + strip_tags(text))
        return

    @staticmethod
    def send_email_message(ids, title, text):
        employees = Employee.objects.filter(id__in=ids)
        for e in employees:
            if e.email:
                send_email(title, text, [e.email])
        return

    def _translate_unicode_punctuations(self, text):
        from bs4 import BeautifulSoup
        return BeautifulSoup(text, 'html')

    @property
    def get_last_education_name(self):
        if not self.education_set.last():
            return ''
        if get_language() == 'ru':
            return self.education_set.last().name_ru
        elif get_language() == 'en':
            return self.education_set.last().name_en
        elif get_language() == 'uz':
            return self.education_set.last().name_ru

    @property
    def get_last_education_speciality(self):
        if not self.education_set.last():
            return ''
        if get_language() == 'ru':
            return self.education_set.last().specialization_ru
        elif get_language() == 'en':
            return self.education_set.last().specialization_en
        elif get_language() == 'uz':
            return self.education_set.last().specialization_ru

    @property
    def get_last_education_other(self):
        if not self.education_set.last():
            return ''
        if get_language() == 'ru':
            return self.education_set.last().additional_ru
        elif get_language() == 'en':
            return self.education_set.last().additional_en
        elif get_language() == 'uz':
            return self.education_set.last().additional_ru

    @property
    def get_primary_language(self):
        return self.language_set.last()

    @property
    def get_languages(self):
        return self.language_set.exclude(id=self.language_set.last().id)[:4]


class EmployeeChanges(models.Model):
    parent = models.OneToOneField(Employee, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, blank=True, verbose_name=_('Created'))
    updated = models.DateTimeField(default=timezone.now, blank=True, verbose_name=_('Updated'))

    full_name_ru = models.CharField(max_length=255, blank=True, verbose_name=_('Fullname ru'))
    full_name_en = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Fullname en'))
    passport_serial = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Passport serial'))
    passport_given_date = models.DateField(null=True, blank=True, verbose_name=_('Passport given date'))
    passport_expires = models.DateField(null=True, blank=True, verbose_name=_('Passport expires'))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('Birth date'))
    birth_place_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Birth place ru'))
    living_address_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Living address ru'))
    inn = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Inn'))
    phone = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Phone'))
    email = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Email'))

    appearance = models.IntegerField(default=0, blank=True, verbose_name=_('Appearance'))
    neatness = models.IntegerField(default=0, blank=True, verbose_name=_('Neatness'))
    skin = models.IntegerField(default=0, blank=True, verbose_name=_('Skin'))
    height = models.FloatField(default=0, blank=True, verbose_name=_('Height'))
    weight = models.FloatField(default=0, blank=True, verbose_name=_('Weight'))
    fatness = models.FloatField(default=0, blank=True, verbose_name=_('Fatness'))
    blood_group = models.IntegerField(default=0, blank=True, verbose_name=_('Blood group'))
    blood_resus = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Blood resus'))
    vision_l = models.FloatField(default=0, blank=True, verbose_name=_('Vision left'))
    vision_r = models.FloatField(default=0, blank=True, verbose_name=_('Vision right'))

    military_duty = models.BooleanField(default=False, blank=True, verbose_name=_('Military duty'))

    wages = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Wages'))
    is_ready_for_university = models.BooleanField(default=False, blank=True, verbose_name=_('Ready for university'))
    criminal_number = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Criminal number'))
    criminal_issue = models.DateField(null=True, blank=True, verbose_name=_('Criminal issue'))
    criminal_comment_ru = models.TextField(default='', blank=True, verbose_name=_('Criminal comment ru'))
    add_spec_signs_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Spec signs ru'))
    hobby_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Hobby ru'))
    other_ru = models.TextField(default='', blank=True, verbose_name=_('Other ru'))

    class Meta:
        db_table = 'employee_changes'
        ordering = ("-id",)
        verbose_name = _('Employee changes')
        verbose_name_plural = _('Employees changes')

    def __str__(self):
        return self.full_name_ru


class EmployeeCountry(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee__countries'
        ordering = ("-id",)

    def __str__(self):
        return self.employee.full_name_ru


class EmployeeChangesCountry(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='changes_countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee__changes__countries'
        ordering = ("-id",)

    def __str__(self):
        return self.employee.full_name_ru
