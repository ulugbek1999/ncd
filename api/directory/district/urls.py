from django.urls import path

from api.directory.district.views import DistrictCreateAPIView, DistrictAPIListView

app_name = 'district'

urlpatterns = [
    path('create/', DistrictCreateAPIView.as_view(), name='create'),
    path('', DistrictAPIListView.as_view(), name='list'),
]
