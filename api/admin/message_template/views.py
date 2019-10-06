from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from api.admin.message_template.serializers import MessageTemplateSerializer
from employee.model.employee import Employee
from message_templates.models import Template, TemplateHistory, EmployeeTemplateHistory, EmployerTemplateHistory
from employer.models import Employer
from bs4 import BeautifulSoup


class MessageTemplateCreateAPIView(CreateAPIView):
    queryset = Template.objects.all()
    serializer_class = MessageTemplateSerializer


class MessageTemplateUpdateAPIView(UpdateAPIView):
    queryset = Template.objects.all()
    serializer_class = MessageTemplateSerializer
    lookup_url_kwarg = 'id'

class MessageTemplateHistoryDeleteApiView(APIView):
    permission_classes = (IsAdminUser, )

    def delete(self, request):
        ids = request.data.get('ids').split(',')
        for i in ids:
            TemplateHistory.objects.get(id=i).delete()
        return Response("Successfully deleted data!", status=status.HTTP_200_OK)


class EmployeeSendMessage(APIView):
    def post(self, request):
        action = request.POST.get('action')
        ids = [int(i) for i in request.POST.getlist('ids')[0].split(',')]
        title = request.POST.get('title')
        text = request.POST.get('text')
        soup = BeautifulSoup(text, 'lxml')
        if action == 'sms':
            Employee.send_sms_message(ids, title, text)
            history = TemplateHistory.objects.create(title=title, text=soup.text, message_type="SMS")
            for i in ids:
                employee = EmployeeTemplateHistory.objects.create(template_history=history, employee=Employee.objects.get(id=i))
        elif action == 'email':
            Employee.send_email_message(ids, title, text)
            history = TemplateHistory.objects.create(title=title, text=soup.text, message_type="Email")
            for i in ids:
                employee = EmployeeTemplateHistory.objects.create(template_history=history, employee=Employee.objects.get(id=i))
        elif action == 'sms&email':
            Employee.send_sms_message(ids, title, text)
            Employee.send_email_message(ids, title, text)
            history_sms = TemplateHistory.objects.create(title=title, text=soup.text, message_type="SMS")
            history_email = TemplateHistory.objects.create(title=title, text=soup.text, message_type="Email")
            for i in ids:
                employee_sms = EmployeeTemplateHistory.objects.create(template_history=history_sms, employee=Employee.objects.get(id=i))
                employee_email = EmployeeTemplateHistory.objects.create(template_history=history_email, employee=Employee.objects.get(id=i))
        return Response()


class EmployerSendMessage(APIView):
    def post(self, request):
        action = request.POST.get('action')
        ids = [int(i) for i in request.POST.getlist('ids')[0].split(',')]
        title = request.POST.get('title')
        text = request.POST.get('text')
        soup = BeautifulSoup(text, 'lxml')
        if action == 'email':
            Employer.send_email_message(ids, title, text)
            history = TemplateHistory.objects.create(title=title, text=soup.text, message_type="Email", isemployer=True)
            for i in ids:
                employer = EmployerTemplateHistory.objects.create(template_history=history, employer=Employer.objects.get(id=i))
        return Response()
