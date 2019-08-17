from rest_framework.generics import ListAPIView, CreateAPIView

from directory.models import District
from api.directory.district.serializers import DistrictSerializer


class DistrictAPIListView(ListAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class DistrictCreateAPIView(CreateAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save(commit=False)
        instance.city_id = self.request.POST.get('city')
        instance.save()
