from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.admin.directory.serializers import (
    CountryCreateSerializer, CountryUpdateSerializer,
    CityCreateSerializer, CityUpdateSerializer,
    DistrictCreateSerializer, DistrictUpdateSerializer,
    LanguageCreateSerializer, LanguageUpdateSerializer,
    EducationTypeCreateSerializer, EducationTypeUpdateSerializer
)

from directory.models import Country, City, District, Language, EducationType


class CountryCreateAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryCreateSerializer


class CountryUpdateAPIView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryUpdateSerializer
    lookup_url_kwarg = 'id'


class CountryDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        Country.objects.filter(id__in=p_ids).delete()
        return Response()


class CityCreateAPIView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityCreateSerializer


class CityUpdateAPIView(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CityUpdateSerializer
    lookup_url_kwarg = 'id'


class CityDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        print(p_ids)
        City.objects.filter(id__in=p_ids).delete()
        return Response()


class DistrictCreateAPIView(CreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictCreateSerializer


class DistrictUpdateAPIView(UpdateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictUpdateSerializer
    lookup_url_kwarg = 'id'


class DistrictDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        District.objects.filter(id__in=p_ids).delete()
        return Response()


class LanguageCreateAPIView(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageCreateSerializer


class LanguageUpdateAPIView(UpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageUpdateSerializer
    lookup_url_kwarg = 'id'


class LanguageDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        Language.objects.filter(id__in=p_ids).delete()
        return Response()


class EducationTypeCreateAPIView(CreateAPIView):
    queryset = EducationType.objects.all()
    serializer_class = EducationTypeCreateSerializer


class EducationTypeUpdateAPIView(UpdateAPIView):
    queryset = EducationType.objects.all()
    serializer_class = EducationTypeUpdateSerializer
    lookup_url_kwarg = 'id'


class EducationTypeDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        EducationType.objects.filter(id__in=p_ids).delete()
        return Response()

