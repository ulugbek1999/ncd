from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.admin.message_template.serializers import MessageTemplateSerializer
from employee.model.employee import Employee
from message_templates.models import Template, TemplateHistory
from partner.models import Partner
from bs4 import BeautifulSoup


class MessageTemplateCreateAPIView(CreateAPIView):
    queryset = Template.objects.all()
    serializer_class = MessageTemplateSerializer


class MessageTemplateUpdateAPIView(UpdateAPIView):
    queryset = Template.objects.all()
    serializer_class = MessageTemplateSerializer
    lookup_url_kwarg = 'id'


class EmployeeSendMessage(APIView):
    def post(self, request):
        action = request.POST.get('action')
        ids = [int(i) for i in request.POST.getlist('ids')[0].split(',')]
        title = request.POST.get('title')
        text = request.POST.get('text')
        soup = BeautifulSoup(text, 'lxml')
        if action == 'sms':
            Employee.send_sms_message(ids, title, text)
            for i in ids:
                TemplateHistory.objects.create(title=title, text=soup.text, employee=Employee.objects.get(id=i), message_type="SMS")
        elif action == 'email':
            Employee.send_email_message(ids, title, text)
            for i in ids:
                TemplateHistory.objects.create(title=title, text=soup.text, employee=Employee.objects.get(id=i), message_type="Email")
        elif action == 'sms&email':
            Employee.send_sms_message(ids, title, text)
            Employee.send_email_message(ids, title, text)
            for i in ids:
                TemplateHistory.objects.create(title=title, text=soup.text, employee=Employee.objects.get(id=i), message_type="SMS")
                TemplateHistory.objects.create(title=title, text=soup.text, employee=Employee.objects.get(id=i), message_type="Email")
        return Response()


class PartnerSendMessage(APIView):
    def post(self, request):
        action = request.POST.get('action')
        ids = [int(i) for i in request.POST.getlist('ids')[0].split(',')]
        title = request.POST.get('title')
        text = request.POST.get('text')
        if action == 'email':
            Partner.send_email_message(ids, title, text)
            for i in ids:
                TemplateHistory.objects.create(title=title, text=text, partner=Partner.objects.get(id=i), message_type="Email", ispartner=True)
        return Response()
