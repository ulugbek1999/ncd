from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language

from employee.file_handlers import reward_file_uploader
from .employee import Employee


class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    name_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Name ru'))
    name_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Name en'))
    description_ru = models.TextField(blank=True, null=True, default='', verbose_name=_('Description ru'))
    description_en = models.TextField(blank=True, null=True, default='', verbose_name=_('Description en'))
    is_new = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'employee__reward'
        verbose_name = _('Reward')
        verbose_name_plural = _('Rewards')

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
    def description(self) -> str:
        if get_language() == 'ru':
            return self.description_ru
        elif get_language() == 'en':
            return self.description_en
        return self.description_ru


class RewardFile(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name="file", verbose_name=_('Reward'))
    file = models.FileField(upload_to=reward_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__reward__file'
        verbose_name = _('Reward file')
        verbose_name_plural = _('Reward files')

    def __str__(self):
        return self.reward.employee.full_name_ru


# -----------------------------------------------------

class RewardChanges(models.Model):
    parent = models.OneToOneField(Reward, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255, blank=True, default='', verbose_name=_('Name ru'))
    description_ru = models.TextField(blank=True, default='', verbose_name=_('Description ru'))

    class Meta:
        db_table = 'employee__reward__changes'
        verbose_name = _('Reward change')
        verbose_name_plural = _('Rewards change')

    def __str__(self):
        return self.parent.employee.full_name_ru

    @property
    def files_count(self):
        return self.file.count()


class RewardChangesFile(models.Model):
    reward = models.ForeignKey(RewardChanges, on_delete=models.CASCADE, related_name="file", verbose_name=_('Reward change'))
    file = models.FileField(upload_to=reward_file_uploader, verbose_name=_('File'))

    class Meta:
        db_table = 'employee__reward__changes__file'
        verbose_name = _('Reward change file')
        verbose_name_plural = _('Reward change files')

    def __str__(self):
        return self.reward.parent.employee.full_name_ru
