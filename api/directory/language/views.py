from rest_framework.generics import ListAPIView, CreateAPIView

from directory.models import Language
from .serializers import LanguageSerializer


class LanguageAPIListView(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageCreateAPIView(CreateAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
