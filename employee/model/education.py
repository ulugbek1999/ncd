from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language

from directory.models import EducationType
from employee.file_handlers import education_file_uploader
from employee.model.employee import Employee


class Education(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    type = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('Education type'))
    name_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Name ru'))
    name_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Name en'))
    address_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Address ru'))
    address_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Address en'))
    specialization_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Specialization ru'))
    specialization_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Specialization en'))
    date_started = models.DateField(null=True, blank=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, blank=True, verbose_name=_('Date finished'))
    additional_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Additional ru'))
    additional_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Additional en'))
    is_new = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'employee__education'
        ordering = ("id", )
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')

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
    def address(self) -> str:
        if get_language() == 'ru':
            return self.address_ru
        elif get_language() == 'en':
            return self.address_en
        return self.address_ru

    @property
    def specialization(self) -> str:
        if get_language() == 'ru':
            return self.specialization_ru
        elif get_language() == 'en':
            return self.specialization_en
        return self.specialization_ru

    @property
    def additional(self) -> str:
        if get_language() == 'ru':
            return self.additional_ru
        elif get_language() == 'en':
            return self.additional_en
        return self.additional_ru

    @property
    def files_count(self):
        return self.file.count()


class EducationFile(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="file", verbose_name=_('Employee'))
    file = models.FileField(upload_to=education_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__education__file'
        ordering = ("-id", )
        verbose_name = _('Education file')
        verbose_name_plural = _('Education files')

    def __str__(self):
        return self.education.employee.full_name_ru


# ------------------------------------------------------------


class EducationChanges(models.Model):

    parent = models.OneToOneField(Education, on_delete=models.CASCADE)
    type = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('Education type'))
    name_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Name ru'))
    address_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Address ru'))
    specialization_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Specialization ru'))
    date_started = models.DateField(null=True, blank=True, verbose_name=_('Date started'))
    date_finished = models.DateField(null=True, blank=True, verbose_name=_('Date finished'))
    additional_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Additional ru'))

    class Meta:
        db_table = 'employee__education__changes'
        ordering = ("-id", )
        verbose_name = _('Education change')
        verbose_name_plural = _('Educations change')

    def __str__(self):
        return self.parent.employee.full_name_ru


class EducationChangesFile(models.Model):
    education = models.ForeignKey(EducationChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Education change'))
    file = models.FileField(upload_to=education_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__education__changes__file'
        ordering = ("-id", )
        verbose_name = _('Education change files')
        verbose_name_plural = _('Education change files')

    def __str__(self):
            return self.education.parent.employee.full_name_ru
