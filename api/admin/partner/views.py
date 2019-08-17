from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.admin.partner.serializers import PartnerCreateSerializer
from employee.model.employee import Employee
from partner.models import Partner, PartnerEmployeeRequest
from utils.mail import send_email
from utils.sms import send_sms


class PartnerCreateAPIView(CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerCreateSerializer


class PartnerDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        Partner.objects.filter(id__in=p_ids).delete()
        return Response()


class PartnerCreateAccountAPIView(APIView):
    def post(self, request, partner_id):
        if not request.data.get('username'):
            raise ValidationError({'username': _('Username is missing')})
        if not request.data.get('password'):
            raise ValidationError({'password': _('Password is missing')})
        if not request.data.get('password_confirm'):
            raise ValidationError({'password_confirm': _('Password confirm is missing')})

        if User.objects.filter(username=request.data.get('username')).count() > 0:
            raise ValidationError({'username': _('Username already exist')})
        if not request.data.get('password') == request.data.get('password_confirm'):
            raise ValidationError({'password_confirm': _('Password didnt match')})

        user = User(username=request.data.get('username'))
        user.set_password(request.data.get('password'))
        user.save()
        partner = Partner.objects.get(id=partner_id)
        partner.user = user
        partner.save()
        send_email(title='', text=f'Ваш логин на uzncd.com: {request.data.get("username")}\nВаш пароль: {request.data.get("password")}', emails=[partner.email, ])
        # send_sms(text=f'your username: {request.data.get("username")}\nyour password: {request.data.get("password")}', number=partner.phone)
        return Response(status=200)


class PartnerEmployeeMakeBusy(APIView):
    def post(self, request):
        emp_id = request.data.get('employee_id')
        try:
            e = Employee.objects.get(id=emp_id)
            if e.busy:
                e.busy = False
                e.save()
            else:
                e.busy = True
                e.save()
            return Response(status=200)
        except Employee.DoesNotExist:
            return Response(status=400)


class PartnerRequestDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        PartnerEmployeeRequest.objects.filter(id__in=p_ids).delete()
        return Response()


class PartnersRequestDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        PartnerEmployeeRequest.objects.filter(partner_id__in=p_ids).delete()
        return Response()
