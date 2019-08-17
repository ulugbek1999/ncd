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


class EmployeeUpdateAPIView(APIView):
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
                education.name_ru['current'] = data.get('name_%d' % i)
                education.address_ru['current'] = data.get('address_%d' % i)
                education.specialization_ru['current'] = data.get('specialization_%d' % i)
                education.date_started['current'] = data.get('date_started_%d' % i),
                education.date_finished['current'] = data.get('date_finished_%d' % i)
                education.additional_ru['current'] = data.get('additional_%d' % i)
                education.save()
                for f in files.getlist('file_%d' % i):
                    file = EducationFile(education=education, file=f)
                    file.save()
                    education.file.add(file)
                    education.save()
            return Response(data={'success': True})
        elif data.get('type') == 'language':
            for i in range(1, amount + 1):
                language = Language()
                language.employee = emp
                language.language_id = data.get('language_%d' % i)
                language.level['current'] = data.get('level_%d' % i)
                language.is_required_to_check = 1 if data.get('is_required_to_check_%d' % i) else 0
                language.save()
                for f in files.getlist('file_%d' % i):
                    file = LanguageFile(language=language, file=f)
                    file.save()
                    language.file.add(file)
                    language.save()
            return Response(data={'success': True})
        elif data.get('type') == 'family':
            for i in range(1, amount + 1):
                family = Family()
                family.employee = emp
                family.status_ru['current'] = data.get('status_%d' % i)
                family.status_en = data.get('status_%d' % i)
                family.children_amount['current'] = data.get('children_amount_%d' % i)
                family.save()
                for f in files.getlist('file_%d' % i):
                    file = FamilyFile(family=family, file=f)
                    file.save()
                    family.file.add(file)
                    family.save()
            return Response(data={'success': True})
        elif data.get('type') == 'army':
            for i in range(1, amount + 1):
                emp.military_duty = True
                emp.save()
                army = Army()
                army.employee = emp
                army.name_ru['current'] = data.get('name_%d', i)
                army.region_ru['current'] = data.get('region_%d', i)
                army.specialization_ru['current'] = data.get('specialization_%d' % i)
                army.date_started['current'] = data.get('date_started_%d' % i)
                army.date_finished['current'] = data.get('date_finished_%d' % i)
                army.rank_ru['current'] = data.get('rank_%d' % i)
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
            for i in range(1, amount + 1):
                reward = Reward()
                reward.employee = emp
                reward.name_ru['current'] = data.get('name_%d' % i)
                reward.description_ru['current'] = data.get('description_%d' % i)
                reward.save()
                for f in files.getlist('file_%d' % i):
                    file = RewardFile(reward=reward, file=f)
                    file.save()
                    reward.file.add(file)
                    reward.save()
            return Response(data={'success': True})
        elif data.get('type') == 'relative':
            for i in range(1, amount + 1):
                relative = Relative()
                relative.employee = emp
                relative.level_ru['current'] = data.get('level_%d' % i)
                relative.level_en = data.get('level_%d' % i)
                relative.fullname_ru['current'] = data.get('fullname_%d' % i)
                relative.birth_date['current'] = data.get('birth_date_%d' % i)
                relative.study_work_place_ru['current'] = data.get('study_work_place_%d' % i)
                relative.position_ru['current'] = data.get('position_%d' % i)
                relative.living_address_ru['current'] = data.get('living_address_%d' % i)
                relative.save()
                for f in files.getlist('file_%d' % i):
                    file = RelativeFile(relative=relative, file=f)
                    file.save()
                    relative.file.add(file)
                    relative.save()
            return Response(data={'success': True})
        elif data.get('type') == 'experience':
            for i in range(1, amount + 1):
                experience = Experience()
                experience.employee = emp
                experience.organization_ru['current'] = data.get('organization_%d' % i)
                experience.date_started['current'] = data.get('date_started_%d' % i)
                experience.date_finished['current'] = data.get('date_finished_%d' % i)
                experience.position_ru['current'] = data.get('position_%d' % i)
                experience.sub_division_ru['current'] = data.get('sub_division_%d' % i)
                experience.address_ru['current'] = data.get('address_%d' % i)
                experience.save()
                for f in files.getlist('file_%d' % i):
                    file = ExperienceFile(experience=experience, file=f)
                    file.save()
                    experience.file.add(file)
                    experience.save()
            return Response(data={'success': True})
        return Response(data={'success': True})
