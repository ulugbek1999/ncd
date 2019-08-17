from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from employee.api.serializers import EmployeeStep2Serializer, EmployeeStep4Serializer, EmployeeStep1Serializer
from employee.model.education import Education, EducationFile
from employee.model.employee import Employee
from employee.model.language import Language, LanguageFile
from employee.model.family import Family, FamilyFile
from employee.model.army import Army, ArmyFile
from employee.model.reward import Reward, RewardFile
from employee.model.relative import Relative, RelativeFile
from employee.model.experience import Experience, ExperienceFile


class Employee1(CreateAPIView):
    serializer_class = EmployeeStep1Serializer
    queryset = Employee.objects.all()
    parser_classes = [FormParser, MultiPartParser]


class Employee2(UpdateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        return EmployeeStep2Serializer

    def get_queryset(self):
        return Employee.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.step_finished = 2
        instance.save()


class Employee3(APIView):
    """employee"""
    # TODO employee_id bilan employeega ulash kerak: done
    # TODO employee ni education,army,family,experience,language,rewardga ulash: done
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        data = request.POST
        files = request.FILES
        emp_id = request.GET.get('id')

        if not emp_id:
            return Response(status=400)
        emp = Employee.objects.filter(id=emp_id)
        if not emp.count() == 1:
            return Response(status=404)
        emp = emp[0]
        emp.step_finished = 3
        emp.save()
        amount = int(data.get('amount'))
        if data.get('type') == 'education':
            for i in range(1, amount+1):
                education = Education(
                    employee=emp,
                    type_id=data.get('type_%d' % i), name_ru=data.get('name_%d' % i), address=data.get('address_%d' % i),
                    specialization=data.get('specialization_%d' % i), date_started=data.get('date_started_%d' % i),
                    date_finished=data.get('date_finished_%d' % i), additional=data.get('additional_%d' % i)
                )
                education.save()
                for f in files.getlist('file_%d' % i):
                    file = EducationFile(education=education, file=f)
                    file.save()
                    education.file.add(file)
                    education.save()
            return Response(data={'success': True})
        elif data.get('type') == 'language':
            for i in range(1, amount+1):
                language = Language(
                    employee=emp, language_id=data.get('language_%d' % i), level=data.get('level_%d' % i),
                    is_required_to_check=1 if data.get('is_required_to_check_%d' % i) else 0
                )
                language.save()
                for f in files.getlist('file_%d' % i):
                    file = LanguageFile(language=language, file=f)
                    file.save()
                    language.file.add(file)
                    language.save()
            return Response(data={'success': True})
        elif data.get('type') == 'family':
            for i in range(1, amount+1):
                family = Family(
                    employee=emp,
                    status=data.get('status_%d' % i), children_amount=data.get('children_amount_%d' % i)
                )
                family.save()
                for f in files.getlist('file_%d' % i):
                    file = FamilyFile(family=family, file=f)
                    file.save()
                    family.file.add(file)
                    family.save()
            return Response(data={'success': True})
        elif data.get('type') == 'army':
            for i in range(1, amount+1):
                emp.military_duty = True
                emp.save()
                army = Army(
                    employee=emp,
                    name=data.get('name_%d', i), region=data.get('region_%d', i),
                    specialization=data.get('specialization_%d' % i), date_started=data.get('date_started_%d' % i),
                    date_finished=data.get('date_finished_%d' % i), rank=data.get('rank_%d' % i)
                )
                if data.get('military_duty'):
                    army.military_duty = 1 if data.get('military_duty') else 0
                army.save()
                for f in files.getlist('file_%d' % i):
                    file = ArmyFile(army=army, file=f)
                    file.save()
                    army.file.add(file)
                    army.save()
            return Response(data={'success': True})
        elif data.get('type') == 'reward':
            for i in range(1, amount+1):
                reward = Reward(
                    employee=emp,
                    name=data.get('name_%d' % i), description=data.get('description_%d' % i)
                )
                reward.save()
                for f in files.getlist('file_%d' % i):
                    file = RewardFile(reward=reward, file=f)
                    file.save()
                    reward.file.add(file)
                    reward.save()
            return Response(data={'success': True})
        elif data.get('type') == 'relative':
            for i in range(1, amount+1):
                relative = Relative(
                    employee=emp,
                    level=data.get('level_%d' % i), fullname=data.get('fullname_%d' % i),
                    birth_date=data.get('birth_date_%d' % i), study_work_place=data.get('study_work_place_%d' % i),
                    position=data.get('position_%d' % i), living_address=data.get('living_address_%d' % i)
                )
                relative.save()
                for f in files.getlist('file_%d' % i):
                    file = RelativeFile(relative=relative, file=f)
                    file.save()
                    relative.file.add(file)
                    relative.save()
            return Response(data={'success': True})
        elif data.get('type') == 'experience':
            for i in range(1, amount+1):
                experience = Experience(
                    employee=emp,
                    organization=data.get('organization_%d' % i), date_started=data.get('date_started_%d' % i),
                    date_finished=data.get('date_finished_%d' % i), position=data.get('position_%d' % i),
                    sub_division=data.get('sub_division_%d' % i), address=data.get('address_%d' % i)
                )
                experience.save()
                for f in files.getlist('file_%d' % i):
                    file = ExperienceFile(experience=experience, file=f)
                    file.save()
                    experience.file.add(file)
                    experience.save()
            return Response(data={'success': True})
        return Response(data={'success': True})


class Employee4(UpdateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        return EmployeeStep4Serializer

    def get_queryset(self):
        return Employee.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.step_finished = 5
        instance.country = ", ".join(i for i in self.request.POST.getlist("country"))
        instance.save()


class Employee4APIView(APIView):

    def post(self, request):
        data = request.POST
        employee = Employee.objects.first()
        employee.wages = data.get('wages')
        employee.country = ', '.join(c for c in data.getlist('country'))
        employee.is_ready_for_universitet = 1 if '1' else False
        employee.criminal_number = data.get('criminal_number')
        employee.criminal_issue = data.get('criminal_issue')
        employee.criminal_comment = data.get('criminal_comment')
        employee.add_spec_signs = data.get('add_spec_signs')
        employee.hobby = data.get('hobby')
        employee.other = data.get('other')
        employee.psycholog = data.get('psycholog')
        employee.save()
        return Response()
