from django.urls import path, include

from api.directory.education_type import views as edu_views

app_name = 'education-type'

urlpatterns = [
    path('create/', edu_views.EducationTypeCreateAPIView.as_view(), name='create'),
    path('', edu_views.EducationTypeAPIListView.as_view(), name='list')
]
