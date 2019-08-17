from rest_framework.generics import ListAPIView, CreateAPIView

from directory.models import City
from api.directory.city.serializers import CitySerializer, CityCreateSerializer


class CityAPIListView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityCreateAPIView(CreateAPIView):
    serializer_class = CityCreateSerializer
    queryset = City.objects.all()
