from django.urls import path
from vacancy.api.views import VacancyRequestDeleteAPIVIew, VacancyRequestDestroyAPIView, SendResponseVacancyAPIView

urlpatterns = [
    path('delete/all', VacancyRequestDeleteAPIVIew.as_view(), name="vacancy_request.delete"),
    path('delete/<int:pk>', VacancyRequestDestroyAPIView.as_view(), name="vacancy_request.destroy"),
    path('send/', SendResponseVacancyAPIView.as_view(), name="send_response.vacancy")
]
