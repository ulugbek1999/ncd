from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .employee import Employee

# TODO Remake model


class Score(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="score", verbose_name="Аппликант")
    birth_year = models.IntegerField(default=0, blank=True)
    education = models.IntegerField(default=0, blank=True)
    language = models.IntegerField(default=0, blank=True)
    medical = models.IntegerField(default=0, blank=True)
    family = models.IntegerField(default=0, blank=True)
    experience = models.IntegerField(default=0, blank=True)
    country = models.IntegerField(default=0, blank=True)
    is_ready_to_university = models.IntegerField(default=0, blank=True)
    criminal_issue = models.IntegerField(default=0, blank=True)
    criminal_other = models.IntegerField(default=0, blank=True)
    wages = models.IntegerField(default=0, blank=True)
    summa = models.FloatField(default=0, blank=True)
    category = models.CharField(max_length=1, blank=True, default="")

    class Meta:
        db_table = "employee_score"
        verbose_name = "Балл"
        verbose_name_plural = "Баллы"

    def __str__(self):
        return self.employee.full_name_ru

    def sum(self):
        if 115.7 <= self.summa <= 136:
            self.category = "A"
            self.save()
            return
        if 95.3 <= self.summa <= 115.6:
            self.category = "B"
            self.save()
            return
        if 74.9 <= self.summa <= 95.2:
            self.category = "C"
            self.save()
            return
        if 54.4 <= self.summa <= 74.8:
            self.category = "D"
            self.save()
            return
