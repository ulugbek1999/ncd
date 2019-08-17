from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from employee.model.employee import Employee
from operators.models import Operator


class Log(models.Model):

    ACTIONS = (
        ("deleted", _("deleted")),
        ("updated", _("updated")),
        ("created", _("created")),
        ("logged_in", _("logged in")),
    )

    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='log')
    created = models.DateTimeField(default=timezone.now, blank=True)
    action = models.CharField(max_length=255, choices=ACTIONS)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "logs"
        ordering = ["-id", ]

    def __str__(self):
        return f'{self.operator.fullname}:::{self.employee.full_name_ru} '
