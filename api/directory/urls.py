from django.urls import path, include

app_name = 'directory'

urlpatterns = [
    path('districts/', include('api.directory.district.urls')),
    path('cities/', include('api.directory.city.urls')),
    path('languages/', include('api.directory.language.urls')),
    path('education-type/', include('api.directory.education_type.urls')),
]
