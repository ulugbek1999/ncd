from django.db import models
from employee.model.employee import Employee
from django.utils.translation import get_language
from django.utils import timezone
import datetime
from django.utils.translation import ugettext_lazy as _
import pytz


utc = pytz.UTC

class CommonInfo(models.Model):
    title_ru = models.CharField(_("Title (ru)"), max_length=50, default="", blank=True)
    title_en = models.CharField(_("Title (en)"), max_length=50, default="", blank=True)
    title_uz = models.CharField(_("Title (uz)"), max_length=50, default="", blank=True)
    title_kz = models.CharField(_("Title (kz)"), max_length=50, default="", blank=True)
    short_description_ru = models.CharField(_("Short description (ru)"), max_length=150, default="", blank=True)
    short_description_en = models.CharField(_("Short description (en)"), max_length=150, default="", blank=True)
    short_description_uz = models.CharField(_("Short description (uz)"), max_length=150, default="", blank=True)
    short_description_kz = models.CharField(_("Short description (kz)"), max_length=150, default="", blank=True)
    description_ru = models.TextField(default="", blank=True)
    description_en = models.TextField(default="", blank=True)
    description_uz = models.TextField(default="", blank=True)
    description_kz = models.TextField(default="", blank=True)

    @property
    def title(self) -> str:
        if get_language() == 'ru':
            return self.title_ru
        elif get_language() == 'en':
            return self.title_en
        elif get_language() == 'kz':
            return self.title_kz
        return self.title_uz
    
    @property
    def short_description(self) -> str:
        if get_language() == 'ru':
            return self.short_description_ru
        elif get_language() == 'en':
            return self.short_description_en
        elif get_language() == 'kz':
            return self.short_description_kz
        return self.short_description_uz

    @property
    def description(self) -> str:
        if get_language() == 'ru':
            return self.description_ru
        elif get_language() == 'en':
            return self.description_en
        elif get_language() == 'kz':
            return self.description_kz
        return self.description_uz


    class Meta:
        abstract = True


class Vacancy(CommonInfo):
    image = models.FileField(blank=True)
    created = models.DateTimeField(_("Created"))
    location_ru = models.CharField(_("Location (ru)"), max_length=100)
    location_uz = models.CharField(_("Location (uz)"), max_length=50)
    location_kz = models.CharField(_("Location (kz)"), max_length=50)
    location_en = models.CharField(_("Location (en)"), max_length=50)
    wages_en = models.CharField(_("Wages (en)"), max_length=50)
    wages_ru = models.CharField(_("Wages (ru)"), max_length=50)
    wages_kz = models.CharField(_("Wages (kz)"), max_length=50)
    wages_uz = models.CharField(_("Wages (uz)"), max_length=50)
    status = models.BooleanField(_("Status"))

    def __str__(self):
        return self.title_en

    @property
    def location(self) -> str:
        if get_language() == 'ru':
            return self.location_ru
        elif get_language() == 'en':
            return self.location_en
        elif get_language() == 'kz':
            return self.location_kz
        return self.location_uz
    
    @property
    def extra(self) -> str:
        if get_language() == 'ru':
            return self.extra_ru
        elif get_language() == 'en':
            return self.extra_en
        elif get_language() == 'kz':
            return self.extra_kz
        return self.extra_uz
    
    @property
    def wages(self) -> str:
        if get_language() == 'ru':
            return self.wages_ru
        elif get_language() == 'en':
            return self.wages_en
        elif get_language() == 'kz':
            return self.wages_kz
        return self.wages_uz    

    def was_published(self):
        now = timezone.now()
        if now - datetime.timedelta(minutes=1) <= self.created <= now:
            return _("Just now")
        elif (now.date() == self.created.date()):
            return _("Today ") + self.created.strftime("%H:%M")
        return self.created.strftime("%d.%m.%Y")
    
    class Meta:
        db_table = "vacancy"
        verbose_name = "vacancy"
        verbose_name_plural = "vacancies"
        ordering = ['-created']


class VacancyRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="vacancy_requests_employee")
    requested_date = models.DateTimeField(_("requested date"), auto_now=True)
    vacancy = models.OneToOneField(Vacancy, on_delete=models.CASCADE, related_name="vacancy_requests")

    class Meta:
        db_table = "vacancy__requests"
        verbose_name = "vacancy"
        verbose_name_plural = "vacancies"
        ordering = ['-requested_date']