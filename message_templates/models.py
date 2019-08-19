from django.db import models
from django.utils.translation import gettext as _
from employee.model.employee import Employee
from partner.models import Partner
from datetime import datetime

TYPE = (
    (1, _('Employee')),
    (2, _('Partner')),
)


class Template(models.Model):
    title = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    type = models.IntegerField(default=1, choices=TYPE, blank=True)

    class Meta:
        db_table = 'templates'
        ordering = ['-id', ]

    def __str__(self):
        return self.text[:50]

class TemplateHistory(models.Model):
    title = models.TextField(blank=True, default='')
    text = models.TextField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_template_history")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name="partner_template_history")
    sent_date = models.DateTimeField(default=datetime.now())
    message_type = models.CharField(max_length=10, blank=True)
    ispartner = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]