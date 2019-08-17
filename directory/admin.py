from django.contrib import admin

from .models import City, District, Country, Language, EducationType


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationType)
class EducationTypeAdmin(admin.ModelAdmin):
    pass
