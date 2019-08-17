from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.html import strip_tags

from employee.model.employee import Employee
from utils.mail import send_email
from utils.sms import send_sms


class PartnerManager(models.Manager):
    def search_filter(self, qs, request):
        """
        :param qs: Employee objects
        :param request: request
        :return: queryset of Employee
        """
        if request.GET.get('boss_fullname'):
            boss_fullname = request.GET.get('boss_fullname')
            qs = qs.filter(boss_fullname__icontains=boss_fullname)
        if request.GET.get('company_name'):
            company_name = request.GET.get('company_name')
            qs = qs.filter(company_name__icontains=company_name)
        return qs


class Partner(models.Model):
    """email field in django user model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='partner')
    company_name = models.TextField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="",
                             verbose_name='Телефон')
    email = models.CharField(max_length=255, default='', blank=True)
    register_number = models.CharField(max_length=255, default='',
                                       verbose_name='Регистрационный номер')
    boss_fullname = models.CharField(max_length=255, default='',
                                     verbose_name='ФИО (первого руководителя)')
    person_fullname_for_hiring = models.CharField(max_length=255, default='',
                                                  verbose_name='ФИО (ответственного лица за наем трудовых мигрантов)')
    legal_address = models.CharField(max_length=255, default='', blank=True,
                                     verbose_name='Юридический адрес')
    workers_amount = models.IntegerField(default=0, blank=True,
                                         verbose_name='Количество работников организации')
    objects = PartnerManager()

    class Meta:
        db_table = "partner"
        ordering = ['-id', ]

    def __str__(self):
        return self.company_name

    @staticmethod
    def send_email_message(ids, title, text):
        employees = Partner.objects.filter(id__in=ids)
        for e in employees:
            if e.email:
                send_email(title, text, [e.email])
        return


class PartnerFile(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    file = models.FileField(upload_to='partner_files/')

    class Meta:
        db_table = 'partner_file'
        ordering = ['-id', ]


class PartnerEmployee(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'partner_employee'
        ordering = ['-id', ]

    def __str__(self):
        return str(self.partner.id)


CONTRACT_TYPE = (
    (1, 'With stamp'),
    (2, 'Online'),
)


class PartnerEmployeeRequest(models.Model):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, blank=True)
    contract_type = models.IntegerField(choices=CONTRACT_TYPE, null=True)

    class Meta:
        db_table = 'partner_employee_request'
        ordering = ['-id', ]
        verbose_name = _('Partner employee request')
        verbose_name_plural = _('Partner employee requests')

    def __str__(self):
        return str(self.partner.id)
