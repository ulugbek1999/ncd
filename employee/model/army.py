from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language

from employee.file_handlers import army_file_uploader
from employee.model.employee import Employee


class Army(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    name_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Name ru'))
    name_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Name en'))
    region_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Region ru'))
    region_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Region en'))
    specialization_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Specialization ru'))
    specialization_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Specialization en'))
    date_started = models.DateField(null=True, blank=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, blank=True, verbose_name=_('Date finished'))
    rank_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Rank ru'))
    rank_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Rank en'))
    is_new = models.BooleanField(default=False, blank=True, null=True,)

    class Meta:
        db_table = 'employee__army'
        ordering = ("-id", )
        verbose_name = _('Military service')
        verbose_name_plural = _('Military services')

    def __str__(self):
        return self.employee.full_name_ru

    @property
    def name(self) -> str:
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        return self.name_ru

    @property
    def region(self) -> str:
        if get_language() == 'ru':
            return self.region_ru
        elif get_language() == 'en':
            return self.region_en
        return self.region_ru

    @property
    def specialization(self) -> str:
        if get_language() == 'ru':
            return self.specialization_ru
        elif get_language() == 'en':
            return self.specialization_en
        return self.specialization_ru

    @property
    def rank(self) -> str:
        if get_language() == 'ru':
            return self.rank_ru
        elif get_language() == 'en':
            return self.rank_en
        return self.rank_ru


class ArmyFile(models.Model):
    army = models.ForeignKey(Army, on_delete=models.CASCADE, related_name="file", verbose_name=_('Military'))
    file = models.FileField(upload_to=army_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__army__file'
        ordering = ("-id", )
        verbose_name = _('Military service file')
        verbose_name_plural = _('Military services files')

    def __str__(self):
        return self.army.employee.full_name_ru


# ---------------------------------------------------------


class ArmyChanges(models.Model):
    parent = models.OneToOneField(Army, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Name ru'))
    region_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Region ru'))
    specialization_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Specialization ru'))
    date_started = models.DateField(null=True, blank=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, blank=True, verbose_name=_('Date finished'))
    rank_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Rank ru'))

    class Meta:
        db_table = 'employee__army__changes'
        ordering = ("-id", )
        verbose_name = _('Military service change')
        verbose_name_plural = _('Military services change')

    def __str__(self):
        return self.parent.employee.full_name_ru


class ArmyChangesFile(models.Model):
    army = models.ForeignKey(ArmyChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Military change'))
    file = models.FileField(upload_to=army_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__army__changes__file'
        ordering = ("-id", )
        verbose_name = _('Military service change file')
        verbose_name_plural = _('Military service change files')

    def __str__(self):
        return self.army.parent.employee.full_name_ru
