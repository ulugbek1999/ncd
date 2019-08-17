from django.db import models
from django.utils.translation import gettext as _
from employee.model.employee import Employee
from partner.models import Partner

MESSAGE_TYPE = (
    (1, _('Employee')),
    (2, _('Partner')),
)


class Template(models.Model):
    title = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    type = models.IntegerField(default=1, choices=MESSAGE_TYPE, blank=True)

    class Meta:
        db_table = 'templates'
        ordering = ['-id', ]

    def __str__(self):
        return self.text[:50]

class TemplateHistory(models.Model):
    title = models.TextField(blank=True, default='')
    text = models.TextField(blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_template_history")
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name="partner_template_history")
    type = models.IntegerField(default=1, choices=MESSAGE_TYPE, blank=True)
    message_type = models.CharField(max_length=20)

    def __str__(self):
        return self.text[:50]