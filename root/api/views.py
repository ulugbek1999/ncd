from django.contrib.auth.models import User
from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.model.army import Army, ArmyFile
from employee.model.education import Education, EducationFile
from employee.model.employee import Employee, EmployeeCountry
from employee.model.experience import Experience, ExperienceFile
from employee.model.family import FamilyFile, Family
from employee.model.language import LanguageFile, Language
from employee.model.relative import Relative, RelativeFile
from employee.model.reward import RewardFile, Reward

from directory.models import Language as DLanguage
from directory.models import City, District, Country

from log.models import Log
from operators.models import OperatorGroup, Operator
from employer.models import Employer
from .serializers import (
    AdminEmployeeUpdate1Serializer, AdminEmployeeUpdate2Serializer,
    AdminEmployeeUpdate4Serializer,
    GroupSerializer,
    OperatorSerializer, EmployerUpdateSerializer, EmployeeTranslationSerializer)


class AdminEmployeeUpdate1(UpdateAPIView):
    serializer_class = AdminEmployeeUpdate1Serializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = "id"


class AdminEmployeeUpdate2(UpdateAPIView):
    serializer_class = AdminEmployeeUpdate2Serializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = "id"


class AdminEmployeeUpdate3Education(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        edu_ids = [i.id for i in emp.education_set.all()]
        try:
            edu_count = data.get("count")
            for i in range(1, int(edu_count)+1):
                edu = Education(
                    employee=emp, type_id=data.get("type_%d" % i), name_ru=data.get("name_%d" % i),
                    address_ru=data.get("address_%d" % i), specialization_ru=data.get("specialization_%d" % i),
                    date_started=data.get("date_started_%d" % i), date_finished=data.get("date_finished_%d" % i),
                    additional_ru=data.get("additional_%d" % i)
                )
                edu.save()
                for j in files.getlist("file_%d" % i):
                    file = EducationFile(education=edu, file=j)
                    file.save()
            Education.objects.filter(id__in=edu_ids).delete()
        except:
            pass
        return response


class AdminEmployeeUpdate3Army(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        army_ids = [i.id for i in emp.army_set.all()]
        try:
            army_count = data.get("count")
            emp.military_duty = data.get("military_duty")
            for i in range(1, int(army_count)+1):
                army = Army(
                    employee=emp, name_ru=data.get("name_%d" % i), region_ru=data.get("region_%d" % i),
                    specialization_ru=data.get("specialization_%d" % i),
                    date_started=data.get("date_started_%d" % i),
                    date_finished=data.get("date_finished_%d" % i), rank_ru=data.get("rank_%d" % i)
                )
                army.save()
                for j in files.getlist("file_%d" % i):
                    file = ArmyFile(army=army, file=j)
                    file.save()
            Army.objects.filter(id__in=army_ids).delete()
        except:
            pass
        return response


class AdminEmployeeUpdate3Language(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        lang_ids = [i.id for i in emp.language_set.all()]
        try:
            lang_count = data.get("count")
            for i in range(1, int(lang_count)+1):
                lang = Language()
                lang.employee = emp
                lang.language_id = data.get("name_%d" % i)
                lang.level = data.get("level_%d" % i)
                lang.is_required_to_check = data.get("is_required_to_check_%d" % i)
                lang.save()
                for j in files.getlist("file_%d" % i):
                    file = LanguageFile(language=lang, file=j)
                    file.save()
            Language.objects.filter(id__in=lang_ids).delete()
        except Exception as e:
            print(e)
        return response


class AdminEmployeeUpdate3Family(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        emp.family.delete()
        try:
            fam_count = data.get("count")
            for i in range(1, int(fam_count)+1):
                fam = Family(
                    employee=emp,
                    status=data.get("status_%d" % i),
                    children_amount=data.get("children_amount_%d" % i)
                )
                fam.save()
                for j in files.getlist("file_%d" % i):
                    file = FamilyFile(family=fam, file=j)
                    file.save()
        except:
            pass
        return response


class AdminEmployeeUpdate3Reward(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        reward_ids = [i.id for i in emp.reward_set.all()]
        try:
            reward_count = data.get("count")
            for i in range(1, int(reward_count)+1):
                reward = Reward(
                    employee=emp, name_ru=data.get("name_%d" % i),
                    description_ru=data.get("description_%d" % i)
                )
                reward.save()
                for j in files.getlist("file_%d" % i):
                    file = RewardFile(reward=reward, file=j)
                    file.save()
            Reward.objects.filter(id__in=reward_ids).delete()
        except:
            pass
        return response


class AdminEmployeeUpdate3Experience(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        exp_ids = [i.id for i in emp.experience_set.all()]
        try:
            exp_count = data.get("count")
            for i in range(1, int(exp_count)+1):
                exp = Experience(
                    employee=emp, organization_ru=data.get("organization_%d" % i), date_started=data.get("date_started_%d" % i),
                    date_finished=data.get("date_finished_%d" % i), position_ru=data.get("position_%d" % i),
                    sub_division_ru=data.get("sub_division_%d" % i), address_ru=data.get("address_%d" % i)
                )
                exp.save()
                for j in files.getlist("file_%d" % i):
                    file = ExperienceFile(experience=exp, file=j)
                    file.save()
            Experience.objects.filter(id__in=exp_ids).delete()
        except:
            pass
        return response


class AdminEmployeeUpdate3Relative(APIView):
    def post(self, request, emp_id):
        response = Response()
        data = request.POST
        files = request.FILES
        emp = Employee.objects.get(id=emp_id)
        rel_ids = [i.id for i in emp.relative_set.all()]
        try:
            rel_count = data.get("count")
            for i in range(1, int(rel_count)+1):
                rel = Relative(
                    employee=emp, level_ru=data.get("level_%d" % i), level_en=data.get("level_%d" % i),
                    fullname_ru=data.get("fullname_%d" % i), birth_date=data.get("birth_date_%d" % i),
                    study_work_place_ru=data.get("study_work_place_%d" % i), position_ru=data.get("position_%d" % i),
                    living_address_ru=data.get("living_address_%d" % i),
                )
                rel.save()
                for j in files.getlist("file_%d"):
                    file = RelativeFile(relative=rel, file=j)
                    file.save()
            Relative.objects.filter(id__in=rel_ids).delete()
        except:
            pass
        return response


class AdminEmployeeUpdate4(UpdateAPIView):
    serializer_class = AdminEmployeeUpdate4Serializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = "id"

    def perform_update(self, serializer):
        instance = serializer.save()
        country_ids = [i for i in self.request.POST.get('country').split(',')]
        EmployeeCountry.objects.filter(employee=instance).delete()
        for i in country_ids:
            if i.isdigit():
                EmployeeCountry.objects.create(employee=instance, country_id=i)
        if self.request.POST.get('level'):
            if self.request.POST.get('level') == 'is_employee':
                instance.is_employee = True
            elif self.request.POST.get('level') == 'is_youth_talent':
                instance.is_youth_talent = True
            elif self.request.POST.get('level') == 'is_student':
                instance.is_student = True
        instance.save()


class GroupCreate(CreateAPIView):
    serializer_class = GroupSerializer
    queryset = OperatorGroup.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.operator1 is not None:
            instance.operator1.operator = 1
            instance.operator1.save()
        if instance.operator2 is not None:
            instance.operator2.operator = 2
            instance.operator2.save()
        if instance.operator3 is not None:
            instance.operator3.operator = 3
            instance.operator3.save()
        if instance.operator4 is not None:
            instance.operator4.operator = 4
            instance.operator4.save()


class GroupUpdate(UpdateAPIView):
    serializer_class = GroupSerializer
    queryset = OperatorGroup.objects.all()
    lookup_url_kwarg = "id"

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.operator1 is not None:
            instance.operator1.operator = 1
            instance.operator1.save()
        if instance.operator2 is not None:
            instance.operator2.operator = 2
            instance.operator2.save()
        if instance.operator3 is not None:
            instance.operator3.operator = 3
            instance.operator3.save()
        if instance.operator4 is not None:
            instance.operator4.operator = 4
            instance.operator4.save()


class OperatorCreate(CreateAPIView):
    serializer_class = OperatorSerializer
    queryset = OperatorGroup.objects.all()

    def perform_create(self, serializer):
        user = User(
            username=self.request.POST.get("username"),
            first_name=self.request.POST.get("firstname"),
            last_name=self.request.POST.get("lastname"),
        )
        user.set_password(self.request.POST.get("password"))
        user.save()
        instance = serializer.save(user=user)
        instance.save()
        if self.request.POST.get("group"):
            gr = OperatorGroup.objects.get(id=self.request.POST.get("group"))
            if instance.operator == 1:
                gr.operator1 = instance
                gr.save()
            elif instance.operator == 2:
                gr.operator2 = instance
                gr.save()
            elif instance.operator == 3:
                gr.operator3 = instance
                gr.save()
            elif instance.operator == 4:
                gr.operator4 = instance
                gr.save()


class OperatorUpdate(UpdateAPIView):
    serializer_class = OperatorSerializer
    queryset = Operator.objects.all()
    lookup_url_kwarg = "id"

    def perform_update(self, serializer):
        instance = serializer.save()
        data = self.request.POST
        username, password = data.get("username"), data.get("password")
        first_name, last_name = data.get("firstname"), data.get("lastname")
        group, operator = data.get("group"), data.get("operator")
        if username:
            instance.user.username = username
            instance.user.save()
        if password:
            instance.user.set_password(password)
            instance.user.save()
        if first_name:
            instance.user.first_name = first_name
            instance.user.save()
        if last_name:
            instance.user.last_name = last_name
            instance.user.save()
        if group:
            g = OperatorGroup.objects.get(id=group)
            if operator:
                if operator == '1': g.operator1 = instance
                if operator == '2': g.operator2 = instance
                if operator == '3': g.operator3 = instance
                if operator == '4': g.operator4 = instance
            g.save()
        if operator:
            instance.operator = operator
        instance.save()


# Employers
class EmployerUpdate(UpdateAPIView):
    serializer_class = EmployerUpdateSerializer
    queryset = Employer.objects.all()
    lookup_url_kwarg = "id"

    def perform_update(self, serializer):
        instance = serializer.save()
        data = self.request.POST
        username, password = data.get("username"), data.get("password")
        email = data.get('email')
        first_name, last_name = data.get("firstname"), data.get("lastname")
        if instance.user is None:
            user = User()
            if username:
                user.username = username
                user.save()
                instance.user = user
                instance.user.save()
            if password:
                user.set_password(password)
                user.save()
                instance.user.set_password(password)
                instance.user.save()
        else:
            if username:
                instance.user.username = username
                instance.user.save()
            if password:
                instance.user.set_password(password)
                instance.user.save()
        if email:
            instance.email = email
            instance.save()
        if first_name:
            instance.user.first_name = first_name
            instance.user.save()
        if last_name:
            instance.user.last_name = last_name
            instance.user.save()
        instance.save()


# Employee Translations
class EmployeeTranslation1(UpdateAPIView):
    serializer_class = EmployeeTranslationSerializer
    lookup_url_kwarg = "id"
    queryset = Employee.objects.all()


# Directory API's
class LanguageCreateAPIView(CreateAPIView):
    serializer_class = ''
    queryset = DLanguage.objects.all()


class CityCreateAPIView(CreateAPIView):
    serializer_class = ''
    queryset = Language.objects.all()


class DistrictCreateAPIView(CreateAPIView):
    serializer_class = ''
    queryset = Language.objects.all()


class CountryCreateAPIView(CreateAPIView):
    serializer_class = ''
    queryset = Language.objects.all()
