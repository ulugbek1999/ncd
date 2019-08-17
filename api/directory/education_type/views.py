from rest_framework.generics import ListAPIView, CreateAPIView

from directory.models import EducationType
from .serializers import EducationTypeSerializer


class EducationTypeAPIListView(ListAPIView):
    serializer_class = EducationTypeSerializer
    queryset = EducationType.objects.all()


class EducationTypeCreateAPIView(CreateAPIView):
    serializer_class = EducationTypeSerializer
    queryset = EducationType.objects.all()
