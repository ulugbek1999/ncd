import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language

from employee.file_handlers import relative_file_uploader
from .employee import Employee


RELATIVE_TYPE = (
    (0, _('Not selected')),
    (1, _('Wife')),
    (2, _('Husband')),
    (3, _('Mother')),
    (4, _('Father')),
    (5, _('Son')),
    (6, _('Dauther')),
    (7, _('Grandmother')),
    (8, _('Grandfather')),
)


class Relative(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    level = models.IntegerField(blank=True, null=True, default=0,  choices=RELATIVE_TYPE, verbose_name=_('Level'))
    fullname_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Fullname ru'))
    fullname_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Fullname en'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Birth date'))
    study_work_place_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Study/work place ru'))
    study_work_place_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Study/work place en'))
    position_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Position ru'))
    position_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Position en'))
    living_address_ru = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Living address ru'))
    living_address_en = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=_('Living address en'))
    is_new = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'employee__relative'
        verbose_name = _('Relative')
        verbose_name_plural = _('Relatives')

    def __str__(self):
        return self.employee.full_name_ru

    @property
    def fullname(self) -> str:
        if get_language() == 'ru':
            return self.fullname_ru
        elif get_language() == 'en':
            return self.fullname_en
        return self.fullname_ru

    @property
    def study_work_place(self) -> str:
        if get_language() == 'ru':
            return self.study_work_place_ru
        elif get_language() == 'en':
            return self.study_work_place_en
        return self.study_work_place_ru

    @property
    def position(self) -> str:
        if get_language() == 'ru':
            return self.position_ru
        elif get_language() == 'en':
            return self.position_en
        return self.position_ru

    @property
    def living_address(self) -> str:
        if get_language() == 'ru':
            return self.living_address_ru
        elif get_language() == 'en':
            return self.living_address_en
        return self.living_address_ru

    @property
    def files_count(self):
        return self.file.count()

    @property
    def age(self):
        return datetime.date.today().year - self.birth_date.year


class RelativeFile(models.Model):
    relative = models.ForeignKey(Relative, on_delete=models.CASCADE, related_name="file", verbose_name=_('Relative'))
    file = models.FileField(upload_to=relative_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__relative__file'
        verbose_name = _('Relative file')
        verbose_name_plural = _('Relative files')

    def __str__(self):
        return self.relative.employee.full_name_ru


# ------------------------------------------------


class RelativeChanges(models.Model):
    parent = models.OneToOneField(Relative, on_delete=models.CASCADE, verbose_name=_('Relative'))
    level = models.IntegerField(null=True, blank=True, choices=RELATIVE_TYPE, verbose_name=_('Level'))
    fullname_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Fullname ru'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Birth date'))
    study_work_place_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Study/work place ru'))
    position_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Position ru'))
    living_address_ru = models.CharField(max_length=255, default='', blank=True, verbose_name=_('Living address ru'))

    class Meta:
        db_table = 'employee__relative__changes'
        verbose_name = _('Relative change')
        verbose_name_plural = _('Relatives change')

    def __str__(self):
        return self.parent.employee.full_name_ru

    @property
    def files_count(self):
        return self.file.count()


class RelativeChangesFile(models.Model):
    relative = models.ForeignKey(RelativeChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Relative change'))
    file = models.FileField(upload_to=relative_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__relative__changes__file'
        verbose_name = _('Relative change file')
        verbose_name_plural = _('Relative change files')

    def __str__(self):
        return self.relative.parent.employee.full_name_ru
