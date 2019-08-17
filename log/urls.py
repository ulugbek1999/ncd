from django.urls import path

from . import views

urlpatterns = [
    path('', views.Logs.as_view(), name='logs'),
]
