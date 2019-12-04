from django.db import models
from django.utils.translation import ugettext_lazy as _

from employee.file_handlers import family_file_uploader
from employee.model.employee import Employee


TYPE = (
    (0, _('Not selected')),
    (1, _('Not married')),
    (2, _('Married')),
    (3, _('Divorced')),
    (4, _('Widower')),
    (5, _('Second marriage')),
    (6, _('Civil marriage')),
)


class Family(models.Model):

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="family", verbose_name=_('Employee'))
    status = models.IntegerField(default=0, choices=TYPE, blank=True, verbose_name=_('Family status'))
    children_amount = models.IntegerField(default=0, blank=True, verbose_name=_('Children amount'))
    is_new = models.BooleanField(default=False, blank=True)

    class Meta:
        db_table = 'employee__family'
        verbose_name = _('Family status')
        verbose_name_plural = _('Family statuses')

    def __str__(self):
        return self.employee.full_name_ru


class FamilyFile(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="fam_file", verbose_name=_('Family'))
    file = models.FileField(upload_to=family_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__family__file'
        verbose_name = _('Family status file')
        verbose_name_plural = _('Family status files')

    def __str__(self):
        return self.family.employee.full_name_ru


# ---------------------------------------------------


class FamilyChanges(models.Model):

    parent = models.OneToOneField(Family, on_delete=models.CASCADE, verbose_name=_('Family'))
    status = models.IntegerField(default=0, choices=TYPE, blank=True, verbose_name=_('Family status'))
    children_amount = models.IntegerField(default=0, blank=True, verbose_name=_('Children amount'))

    class Meta:
        db_table = 'employee__family__changes'
        verbose_name = _('Family status change')
        verbose_name_plural = _('Family statuses change')

    def __str__(self):
        return self.parent.employee.full_name_ru

    @property
    def files_count(self):
        return self.file.count()


class FamilyChangesFile(models.Model):
    family = models.ForeignKey(FamilyChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Family status change'))
    file = models.FileField(upload_to=family_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__family__changes__file'
        verbose_name = _('Family status change file')
        verbose_name_plural = _('Family status change files')

    def __str__(self):
        return self.family.parent.employee.full_name_ru
