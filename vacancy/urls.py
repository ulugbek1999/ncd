from django.urls import path
from .views import VacancyRequestListView, VacancyRequestDetailView


urlpatterns = [
    path('list/', VacancyRequestListView.as_view(), name="root.vacancy.list"),
    path('detail/<int:pk>', VacancyRequestDetailView.as_view(), name='vacancy.detail'),
]
