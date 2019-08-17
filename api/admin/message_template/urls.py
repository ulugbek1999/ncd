from django.urls import path

from .views import MessageTemplateCreateAPIView, EmployeeSendMessage, PartnerSendMessage,\
    MessageTemplateUpdateAPIView

app_name = 'template'


urlpatterns = [
    path('create', MessageTemplateCreateAPIView.as_view(), name='create'),
    path('update/<int:id>/', MessageTemplateUpdateAPIView.as_view(), name='update'),
    path('employee/send/', EmployeeSendMessage.as_view(), name='employee.send'),
    path('partner/send/', PartnerSendMessage.as_view(), name='partner.send'),
]
