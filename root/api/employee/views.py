from rest_framework.generics import UpdateAPIView

from employee.model.education import Education
from employee.model.army import Army
from employee.model.employee import Employee
from employee.model.relative import Relative
from employee.model.experience import Experience
from employee.model.reward import Reward

from .serializers import (
    EducationTranslateSerializer, RewardTranslateSerializer, RelativeTranslateSerializer,
    ExperienceTranslateSerializer, ArmyTranslateSerializer
)

from .serializers import (
    EmployeeTranslate1Serializer, EmployeeTranslate4Serializer
)


# ************************************ Employee 1 Translate ************************************ #
class EmployeeTranslate1UpdateView(UpdateAPIView):
    serializer_class = EmployeeTranslate1Serializer
    lookup_url_kwarg = 'id'
    queryset = Employee.objects.all()


# ************************************ Employee 3 Translate ************************************ #
class EducationTranslateUpdate(UpdateAPIView):
    serializer_class = EducationTranslateSerializer
    lookup_url_kwarg = 'id'
    queryset = Education.objects.all()


class ArmyTranslateUpdate(UpdateAPIView):
    serializer_class = ArmyTranslateSerializer
    lookup_url_kwarg = 'id'
    queryset = Army.objects.all()


class RelativeTranslateUpdate(UpdateAPIView):
    serializer_class = RelativeTranslateSerializer
    lookup_url_kwarg = 'id'
    queryset = Relative.objects.all()


class ExperienceTranslateUpdate(UpdateAPIView):
    serializer_class = ExperienceTranslateSerializer
    lookup_url_kwarg = 'id'
    queryset = Experience.objects.all()


class RewardTranslateUpdate(UpdateAPIView):
    serializer_class = RewardTranslateSerializer
    lookup_url_kwarg = 'id'
    queryset = Reward.objects.all()


# ************************************ Employee 4 Translate ************************************ #
class EmployeeTranslate4UpdateView(UpdateAPIView):
    serializer_class = EmployeeTranslate4Serializer
    lookup_url_kwarg = 'id'
    queryset = Employee.objects.all()
