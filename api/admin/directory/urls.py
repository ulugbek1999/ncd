from django.urls import path

from api.admin.directory.views import (
    LanguageCreateAPIView, LanguageUpdateAPIView, LanguageDeleteAPIView,
    CityCreateAPIView, CityUpdateAPIView, CityDeleteAPIView,
    CountryCreateAPIView, CountryUpdateAPIView, CountryDeleteAPIView,
    DistrictCreateAPIView, DistrictUpdateAPIView, DistrictDeleteAPIView,
    EducationTypeCreateAPIView, EducationTypeUpdateAPIView, EducationTypeDeleteAPIView)

app_name = 'directory'

urlpatterns = [
    path('country/create/', CountryCreateAPIView.as_view(), name='country.create'),
    path('country/update/<int:id>/', CountryUpdateAPIView.as_view(), name='country.update'),
    path('country/delete/', CountryDeleteAPIView.as_view(), name='country.delete'),

    path('city/create/', CityCreateAPIView.as_view(), name='city.create'),
    path('city/update/<int:id>/', CityUpdateAPIView.as_view(), name='city.update'),
    path('city/delete/', CityDeleteAPIView.as_view(), name='city.delete'),

    path('district/create/', DistrictCreateAPIView.as_view(), name='district.create'),
    path('district/update/<int:id>/', DistrictUpdateAPIView.as_view(), name='district.update'),
    path('district/delete/', DistrictDeleteAPIView.as_view(), name='district.delete'),

    path('language/create/', LanguageCreateAPIView.as_view(), name='language.create'),
    path('language/update/<int:id>/', LanguageUpdateAPIView.as_view(), name='language.update'),
    path('language/delete/', LanguageDeleteAPIView.as_view(), name='language.delete'),

    path('education/create/', EducationTypeCreateAPIView.as_view(), name='education.create'),
    path('education/update/<int:id>/', EducationTypeUpdateAPIView.as_view(), name='education.update'),
    path('education/delete/', EducationTypeDeleteAPIView.as_view(), name='education.delete'),
]
