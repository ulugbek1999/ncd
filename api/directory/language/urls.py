from django.urls import path

from api.directory.language.views import LanguageCreateAPIView, LanguageAPIListView

app_name = 'language'

urlpatterns = [
    path('create/', LanguageCreateAPIView.as_view(), name='create'),
    path('', LanguageAPIListView.as_view(), name='list')
]
