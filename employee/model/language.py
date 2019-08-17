from django.db import models
from django.utils.translation import ugettext_lazy as _

from directory.models import Language as Lang
from employee.file_handlers import language_file_uploader
from .employee import Employee


LEVEL = (
    (1, _('Best')),
    (2, _('Good')),
    (3, _('Not bad'))
)


class Language(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    language = models.ForeignKey(Lang, on_delete=models.CASCADE, verbose_name=_('Language'))
    level = models.IntegerField(default=0, blank=True, choices=LEVEL, verbose_name=_('Level'))
    is_required_to_check = models.BooleanField(blank=True, default=False, verbose_name=_('Must be checked'))
    is_new = models.BooleanField(default=False, blank=True)

    class Meta:
        db_table = 'employee__language'
        ordering = ("id", )
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return self.employee.full_name_ru


class LanguageFile(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="file", verbose_name=_('Language'))
    file = models.FileField(upload_to=language_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__language__file'
        ordering = ("-id", )
        verbose_name = _('Language file')
        verbose_name_plural = _('Language files')

    def __str__(self):
        return self.language.employee.full_name_ru


# -----------------------------------------------------


class LanguageChanges(models.Model):
    parent = models.OneToOneField(Language, on_delete=models.CASCADE)
    language = models.ForeignKey(Lang, on_delete=models.CASCADE, verbose_name=_('Language'))
    level = models.IntegerField(default=0, blank=True, choices=LEVEL, verbose_name=_('Level'))
    is_required_to_check = models.BooleanField(blank=True, default=False, verbose_name=_('Must be checked'))

    class Meta:
        db_table = 'employee__language__changes'
        ordering = ("id", )
        verbose_name = _('Language change')
        verbose_name_plural = _('Languages change')

    def __str__(self):
        return self.parent.employee.full_name_ru


class LanguageChangesFile(models.Model):
    language = models.ForeignKey(LanguageChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Language change'))
    file = models.FileField(upload_to=language_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__language__changes__file'
        ordering = ("-id", )
        verbose_name = _('Language change file')
        verbose_name_plural = _('Language change files')

    def __str__(self):
        return self.language.parent.employee.full_name_ru
