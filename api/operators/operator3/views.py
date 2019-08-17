from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.model.army import Army, ArmyFile
from employee.model.education import Education, EducationFile
from employee.model.employee import Employee
from employee.model.experience import Experience, ExperienceFile
from employee.model.family import Family, FamilyFile
from employee.model.language import Language, LanguageFile
from employee.model.relative import Relative, RelativeFile
from employee.model.reward import Reward, RewardFile
from log.models import Log


class EmployeeCreate(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request, id):
        data = request.POST
        files = request.FILES

        emp = Employee.objects.filter(id=id)
        if not emp.count() == 1:
            return Response(status=404)
        emp = emp[0]
        emp.step_finished = 3
        Log.objects.create(operator=self.request.user.operator, action='created', employee_id=emp.id)
        emp.save()
        amount = int(data.get('amount'))
        if data.get('type') == 'education':
            for i in range(1, amount + 1):
                education = Education()
                education.employee = emp
                education.type_id = data.get('type_%d' % i)
                education.name_ru = data.get('name_%d' % i)
                education.address_ru = data.get('address_%d' % i)
                education.specialization_ru = data.get('specialization_%d' % i)
                education.date_started = data.get('date_started_%d' % i)
                education.date_finished = data.get('date_finished_%d' % i)
                education.additional_ru = data.get('additional_%d' % i)
                education.save()
                for f in files.getlist('file_%d' % i):
                    file = EducationFile(education=education, file=f)
                    file.save()
            return Response(data={'success': True})
        elif data.get('type') == 'language':
            for i in range(1, amount + 1):
                language = Language()
                language.employee = emp
                language.language_id = data.get('language_%d' % i)
                language.level = data.get('level_%d' % i)
                language.is_required_to_check = 1 if data.get('is_required_to_check_%d' % i) == 'true' else 0
                language.save()
                for f in files.getlist('file_%d' % i):
                    file = LanguageFile(language=language, file=f)
                    file.save()
            return Response(data={'success': True})
        elif data.get('type') == 'family':
            if amount == 0:
                family = Family(status=0, children_amount=0)
                family.save()
            else:
                for i in range(1, amount + 1):
                    family = Family()
                    family.employee = emp
                    family.status = data.get('status_%d' % i)
                    family.children_amount = data.get('children_amount_%d' % i)
                    family.save()
                    for f in files.getlist('file_%d' % i):
                        file = FamilyFile(family=family, file=f)
                        file.save()
            return Response(data={'success': True})
        elif data.get('type') == 'army':
            for i in range(1, amount + 1):
                emp.military_duty = True
                emp.save()
                army = Army()
                army.employee = emp
                army.name_ru = data.get('name_%d' % i)
                army.region_ru = data.get('region_%d' % i)
                army.specialization_ru = data.get('specialization_%d' % i)
                army.date_started = data.get('date_started_%d' % i)
                army.date_finished = data.get('date_finished_%d' % i)
                army.rank_ru = data.get('rank_%d' % i)
                if data.get('military_duty'):
                    army.military_duty = 1 if data.get('military_duty') == 'on' else 0
                army.save()
                for f in files.getlist('file_%d' % i):
                    file = ArmyFile(army=army, file=f)
                    file.save()
            return Response(data={'success': True})
        elif data.get('type') == 'reward':
            for i in range(1, amount + 1):
                reward = Reward()
                reward.employee = emp
                reward.name_ru = data.get('name_%d' % i)
                reward.description_ru = data.get('description_%d' % i)
                reward.save()
                for f in files.getlist('file_%d' % i):
                    file = RewardFile(reward=reward, file=f)
                    file.save()
            return Response(data={'success': True})
        elif data.get('type') == 'relative':
            for i in range(1, amount + 1):
                relative = Relative()
                relative.employee = emp
                relative.level = data.get('level_%d' % i)
                relative.fullname_ru = data.get('fullname_%d' % i)
                relative.birth_date = data.get('birth_date_%d' % i)
                relative.study_work_place_ru = data.get('study_work_place_%d' % i)
                relative.position_ru = data.get('position_%d' % i)
                relative.living_address_ru = data.get('living_address_%d' % i)
                relative.save()
                for f in files.getlist('file_%d' % i):
                    file = RelativeFile(relative=relative, file=f)
                    file.save()
                    # relative.file.add(file)
                    # relative.save()
            return Response(data={'success': True})
        elif data.get('type') == 'experience':
            for i in range(1, amount + 1):
                experience = Experience()
                experience.employee = emp
                experience.organization_ru = data.get('organization_%d' % i)
                experience.date_started = data.get('date_started_%d' % i)
                experience.date_finished = data.get('date_finished_%d' % i)
                experience.position_ru = data.get('position_%d' % i)
                experience.sub_division_ru = data.get('sub_division_%d' % i)
                experience.address_ru = data.get('address_%d' % i)
                experience.save()
                for f in files.getlist('file_%d' % i):
                    file = ExperienceFile(experience=experience, file=f)
                    file.save()
            return Response(data={'success': True})
        return Response(data={'success': True})
