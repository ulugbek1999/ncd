from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.MessageTemplateCreate.as_view(), name='template.create'),
]