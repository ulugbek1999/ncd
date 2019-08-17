from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.admin.employee.serializers import Employee1Serializer, Employee2Serializer, Employee4Serializer
from employee.model.army import ArmyFile
from employee.model.education import EducationFile
from employee.model.employee import Employee
from employee.model.experience import ExperienceFile
from employee.model.language import LanguageFile
from employee.model.relative import RelativeFile
from employee.model.reward import RewardFile


class Employee1Update(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee1Serializer
    lookup_url_kwarg = 'id'


class Employee2Update(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee2Serializer
    lookup_url_kwarg = 'id'


class Employee4Update(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee4Serializer
    lookup_url_kwarg = 'id'


class EmployeeDeleteView(APIView):
    def post(self, request):
        ids = request.POST.get('ids')
        if not ids:
            return Response(status=400)
        ids = [int(i) for i in ids.split(',') if i.isdigit()]
        user_ids = []
        emp_ids = []
        for i in Employee.objects.filter(id__in=ids):
            if i.user is not None:
                user_ids.append(i.user.id)
            else:
                i.delete()
        # user_ids = [i.user.id for i in Employee.objects.filter(id__in=ids) if i.user is not None]

        User.objects.filter(id__in=user_ids).delete()
        return Response(status=200)


class EmployeeApplyChanges(APIView):
    def post(self, request):
        emp_id = request.POST.get('id')
        emp = Employee.objects.get(id=emp_id)
        # employee changes
        if hasattr(emp, 'employeechanges'):
            fields = emp._meta.get_fields()
            for f in fields:
                if f.name == 'id':
                    continue
                if hasattr(emp.employeechanges, f.name):
                    attr = getattr(emp.employeechanges, f.name)
                    if attr is not None and not attr == '':
                        setattr(emp, f.name, getattr(emp.employeechanges, f.name))
            emp.employeechanges.delete()
            emp.save()
        # education changes
        for edu in emp.education_set.all():
            if hasattr(edu, 'educationchanges'):
                fields = edu._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(edu.educationchanges, f.name):
                            edu.file.all().delete()
                            for file in getattr(edu.educationchanges, f.name).all():
                                EducationFile.objects.create(education=edu, file=file.file)
                                file.delete()
                        continue
                    if hasattr(edu.educationchanges, f.name):
                        attr = getattr(edu.educationchanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(edu, f.name, attr)
                edu.educationchanges.delete()
                edu.save()
        # language changes
        for lang in emp.language_set.all():
            if hasattr(lang, 'languagechanges'):
                fields = lang._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(lang.languagechanges, f.name):
                            lang.file.all().delete()
                            for file in getattr(lang.languagechanges, f.name).all():
                                LanguageFile.objects.create(language=lang, file=file.file)
                                file.delete()
                        continue
                    if hasattr(lang.languagechanges, f.name):
                        attr = getattr(lang.languagechanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(lang, f.name, attr)
                lang.languagechanges.delete()
                lang.save()
        # army changes
        for army in emp.army_set.all():
            if hasattr(army, 'armychanges'):
                fields = army._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(army.armychanges, f.name):
                            army.file.all().delete()
                            for file in getattr(army.armychanges, f.name).all():
                                ArmyFile.objects.create(army=army, file=file.file)
                                file.delete()
                        continue
                    if hasattr(army.armychanges, f.name):
                        attr = getattr(army.armychanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(army, f.name, attr)
                army.armychanges.delete()
                army.save()
        # # family changes
        if hasattr(emp, 'family'):
            if hasattr(emp.family, 'familychanges'):
                fields = emp.family._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(emp.family.familychanges, f.name):
                            emp.family.file.all().delete()
                            for file in getattr(emp.family.familychanges, f.name).all():
                                RewardFile.objects.create(family=emp.family, file=file.file)
                                file.delete()
                        continue
                    if hasattr(emp.family.familychanges, f.name):
                        attr = getattr(emp.family.familychanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(emp.family, f.name, attr)
                emp.family.familychanges.delete()
                emp.family.save()
        # reward changes
        for reward in emp.reward_set.all():
            if hasattr(reward, 'rewardchanges'):
                fields = reward._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(reward.rewardchanges, f.name):
                            reward.file.all().delete()
                            for file in getattr(reward.rewardchanges, f.name).all():
                                RewardFile.objects.create(reward=reward, file=file.file)
                                file.delete()
                        continue
                    if hasattr(reward.rewardchanges, f.name):
                        attr = getattr(reward.rewardchanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(reward, f.name, attr)
                reward.rewardchanges.delete()
                reward.save()
        # relative changes
        for rel in emp.relative_set.all():
            if hasattr(rel, 'relativechanges'):
                fields = rel._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(rel.relativechanges, f.name):
                            rel.file.all().delete()
                            for file in getattr(rel.relativechanges, f.name).all():
                                RelativeFile.objects.create(relative=rel, file=file.file)
                                file.delete()
                        continue
                    if hasattr(rel.relativechanges, f.name):
                        attr = getattr(rel.relativechanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(rel, f.name, attr)
                rel.relativechanges.delete()
                rel.save()
        # experience changes
        for exp in emp.experience_set.all():
            if hasattr(exp, 'experiencechanges'):
                fields = exp._meta.get_fields()
                for f in fields:
                    if f.name == 'id':
                        continue
                    if f.name == 'file':
                        if hasattr(exp.experiencechanges, f.name):
                            exp.file.all().delete()
                            for file in getattr(exp.experiencechanges, f.name).all():
                                ExperienceFile.objects.create(experience=exp, file=file.file)
                                file.delete()
                        continue
                    if hasattr(exp.experiencechanges, f.name):
                        attr = getattr(exp.experiencechanges, f.name)
                        if attr is not None and not attr == '':
                            setattr(exp, f.name, attr)
                exp.experiencechanges.delete()
                exp.save()
        return Response()


class EmployeeDeleteChanges(APIView):
    def post(self, request):
        emp_id = request.POST.get('id')
        emp = Employee.objects.get(id=emp_id)
        # employee changes
        if hasattr(emp, 'employeechanges'):
            emp.employeechanges.delete()
        # education changes
        for edu in emp.education_set.all():
            if hasattr(edu, 'educationchanges'):
                edu.educationchanges.delete()
        # language changes
        for lang in emp.language_set.all():
            if hasattr(lang, 'languagechanges'):
                lang.languagechanges.delete()
        # army changes
        for army in emp.army_set.all():
            if hasattr(army, 'armychanges'):
                army.armychanges.delete()
        # family changes
        if hasattr(emp, 'family'):
            if hasattr(emp.family, 'familychanges'):
                emp.family.familychanges.delete()
        # reward changes
        for reward in emp.reward_set.all():
            if hasattr(reward, 'rewardchanges'):
                reward.rewardchanges.delete()
        # relative changes
        for rel in emp.relative_set.all():
            if hasattr(rel, 'relativechanges'):
                rel.relativechanges.delete()
        # experience changes
        for exp in emp.experience_set.all():
            if hasattr(exp, 'experiencechanges'):
                exp.experiencechanges.delete()
        return Response()


class EmployeeChangePasswordAPIView(APIView):
    def post(self, request, emp_id):
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        emp = Employee.objects.filter(id=emp_id)
        if emp.count() == 1:
            user = User.objects.filter(id=emp[0].user_id)
            if user.count() == 1:
                if password == password_confirm:
                    user[0].set_password(password)
                    user[0].save()
                    return Response()
                raise ValidationError({'error': _('Password didnt match')})
            raise ValidationError({'error': _('Employee not found')})
        raise ValidationError({'error': _('Employee not found')})


class Employee3OperatorDeleteView(APIView):
    def post(self, request):
        from django.apps import apps
        model_type = request.POST.get('model_name')
        model_id = request.POST.get('model_id')
        apps.get_model(app_label='employee', model_name=model_type).objects.filter(id=model_id).delete()
        return Response()
