from django.db import models
from django.utils.translation import get_language


class City(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    class Meta:
        db_table = 'directory_city'
        ordering = ['-id', ]

    def __str__(self):
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        elif get_language() == 'uz':
            return self.name_ru
        return self.name_ru

    @property
    def name(self) -> str:
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        return self.name_ru


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='district')
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        db_table = 'directory_district'
        ordering = ['-id', ]

    def __str__(self):
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        elif get_language() == 'uz':
            return self.name_ru
        return self.name_ru


class Country(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    score = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_country'
        ordering = ['-id', ]

    def __str__(self):
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        elif get_language() == 'uz':
            return self.name_ru
        return self.name_ru

    @property
    def name(self) -> str:
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        return self.name_ru


class Language(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    excellent = models.IntegerField(default=0, blank=True)
    good = models.IntegerField(default=0, blank=True)
    not_bad = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_language'
        ordering = ['-id', ]

    def __str__(self):
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        elif get_language() == 'uz':
            return self.name_ru
        return self.name_ru

    @property
    def name(self) -> str:
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        return self.name_ru


class EducationType(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    score = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_education_type'
        ordering = ['-id', ]

    def __str__(self):
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        elif get_language() == 'uz':
            return self.name_ru
        return self.name_ru

    @property
    def name(self) -> str:
        if get_language() == 'ru':
            return self.name_ru
        elif get_language() == 'en':
            return self.name_en
        return self.name_ru
