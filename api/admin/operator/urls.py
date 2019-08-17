from django.urls import path

from .views import OperatorGroupDeleteView, OperatorDeleteView, OperatorChangeUsernamePassword

app_name = 'operator'

urlpatterns = [
    path('group-delete/', OperatorGroupDeleteView.as_view(), name='operator-group.delete'),
    path('operator-delete/', OperatorDeleteView.as_view(), name='operator.delete'),
    path('operator-change-username-password/<int:user_id>/', OperatorChangeUsernamePassword.as_view(),
         name='operator.username.password')
]
