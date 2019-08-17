from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language

from employee.file_handlers import experience_file_uploader
from employee.model.employee import Employee


class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    organization_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Organization name ru'))
    organization_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Organization name en'))
    date_started = models.DateField(null=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, verbose_name=_('Date finished'))
    position_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Position ru'))
    position_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Position en'))
    sub_division_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Sub division ru'))
    sub_division_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Sub division en'))
    address_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Address ru'))
    address_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Address en'))
    is_new = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'employee__experience'
        ordering = ("-id", )
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')

    def __str__(self):
        return self.employee.full_name_ru

    @property
    def organization(self) -> str:
        if get_language() == 'ru':
            return self.organization_ru
        elif get_language() == 'en':
            return self.organization_en
        return self.organization_ru

    @property
    def position(self) -> str:
        if get_language() == 'ru':
            return self.position_ru
        elif get_language() == 'en':
            return self.position_en
        return self.position_ru

    @property
    def sub_division(self) -> str:
        if get_language() == 'ru':
            return self.sub_division_ru
        elif get_language() == 'en':
            return self.sub_division_en
        return self.sub_division_ru

    @property
    def address(self) -> str:
        if get_language() == 'ru':
            return self.address_ru
        elif get_language() == 'en':
            return self.address_en
        return self.address_ru

    @property
    def files_count(self):
        return self.file.count()


class ExperienceFile(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="file", verbose_name=_('Experience'))
    file = models.FileField(upload_to=experience_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__experience__file'
        ordering = ("-id", )
        verbose_name = _('Experience file')
        verbose_name_plural = _('Experience files')

    def __str__(self):
        return self.experience.employee.full_name_ru


# -----------------------------------------------------------


class ExperienceChanges(models.Model):
    parent = models.OneToOneField(Experience, on_delete=models.CASCADE)
    organization_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Organization name ru'))
    date_started = models.DateField(null=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, verbose_name=_('Date finished'))
    position_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Position ru'))
    sub_division_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Sub division ru'))
    address_ru = models.CharField(max_length=255, blank=True, default='', verbose_name=_('Address ru'))

    class Meta:
        db_table = 'employee__experience__changes'
        ordering = ("-id", )
        verbose_name = _('Experience change')
        verbose_name_plural = _('Experience changes')

    def __str__(self):
        return self.parent.employee.full_name_ru


class ExperienceChangesFile(models.Model):
    experience = models.ForeignKey(ExperienceChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Experience change'))
    file = models.FileField(upload_to=experience_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__experience__changes__file'
        ordering = ("-id", )
        verbose_name = _('Experience change file')
        verbose_name_plural = _('Experience change files')

    def __str__(self):
        return self.experience.parent.employee.full_name_ru
