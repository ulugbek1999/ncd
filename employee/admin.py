from django.contrib import admin

from employee.model.employee import Employee, EmployeeCountry, EmployeeChanges, EmployeeChangesCountry
from employee.model.education import Education, EducationFile, EducationChanges, EducationChangesFile
from employee.model.army import Army, ArmyFile, ArmyChanges, ArmyChangesFile
from employee.model.experience import Experience, ExperienceFile, ExperienceChanges, ExperienceChangesFile
from employee.model.family import Family, FamilyFile, FamilyChanges, FamilyChangesFile
from employee.model.language import Language, LanguageFile, LanguageChanges, LanguageChangesFile
from employee.model.relative import Relative, RelativeFile, RelativeChanges, RelativeChangesFile
from employee.model.reward import Reward, RewardFile, RewardChanges, RewardChangesFile
from employee.model.score import Score


# employee
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeCountry)
class EmployeeCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeChanges)
class EmployeeChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeChangesCountry)
class EmployeeChangesCountryAdmin(admin.ModelAdmin):
    pass


# education
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationFile)
class EducationFileAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationChanges)
class EducationChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationChangesFile)
class EducationChangesFileAdmin(admin.ModelAdmin):
    pass


# army
@admin.register(Army)
class ArmyAdmin(admin.ModelAdmin):
    pass


@admin.register(ArmyFile)
class ArmyFileAdmin(admin.ModelAdmin):
    pass


@admin.register(ArmyChanges)
class ArmyChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(ArmyChangesFile)
class ArmyChangesFileAdmin(admin.ModelAdmin):
    pass


# experience
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceFile)
class ExperienceFileAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceChanges)
class ExperienceChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceChangesFile)
class ExperienceChangesFileAdmin(admin.ModelAdmin):
    pass


# family
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(FamilyFile)
class FamilyFileAdmin(admin.ModelAdmin):
    pass


@admin.register(FamilyChanges)
class FamilyChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(FamilyChangesFile)
class FamilyChangesFileAdmin(admin.ModelAdmin):
    pass


# language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageFile)
class LanguageFileAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageChanges)
class LanguageChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageChangesFile)
class LanguageChangesFileAdmin(admin.ModelAdmin):
    pass


# relative
@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    pass


@admin.register(RelativeFile)
class RelativeFileAdmin(admin.ModelAdmin):
    pass


@admin.register(RelativeChanges)
class RelativeChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(RelativeChangesFile)
class RelativeChangesFileAdmin(admin.ModelAdmin):
    pass


# reward
@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass


@admin.register(RewardFile)
class RewardFileAdmin(admin.ModelAdmin):
    pass


@admin.register(RewardChanges)
class RewardChangesAdmin(admin.ModelAdmin):
    pass


@admin.register(RewardChangesFile)
class RewardChangesFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
