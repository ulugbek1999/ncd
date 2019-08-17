from django.urls import path

from api.foreign_api.views import UserCreateAPIView

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view()),
]
