from django.urls import path

from .views import MessageTemplateCreateAPIView, EmployeeSendMessage, EmployerSendMessage,\
    MessageTemplateUpdateAPIView, MessageTemplateHistoryDeleteApiView

app_name = 'template'


urlpatterns = [
    path('create', MessageTemplateCreateAPIView.as_view(), name='create'),
    path('update/<int:id>/', MessageTemplateUpdateAPIView.as_view(), name='update'),
    path('employee/send/', EmployeeSendMessage.as_view(), name='employee.send'),
    path('employer/send/', EmployerSendMessage.as_view(), name='employer.send'),
    path('message_template_history/delete/', MessageTemplateHistoryDeleteApiView.as_view(), name="template_history.delete")
]
