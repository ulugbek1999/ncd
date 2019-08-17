from django.urls import path

from api.directory.city.views import CityCreateAPIView, CityAPIListView

app_name = 'city'

urlpatterns = [
    path('create/', CityCreateAPIView.as_view(), name='create'),
    path('', CityAPIListView.as_view(), name='list'),
]
