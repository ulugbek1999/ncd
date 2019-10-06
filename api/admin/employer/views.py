from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.admin.employer.serializers import EmployerCreateSerializer
from employee.model.employee import Employee
from employer.models import Employer, EmployerEmployeeRequest
from utils.mail import send_email
from utils.sms import send_sms


class EmployerCreateAPIView(CreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerCreateSerializer


class EmployerDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        Employer.objects.filter(id__in=p_ids).delete()
        return Response()


class EmployerCreateAccountAPIView(APIView):
    def post(self, request, employer_id):
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
        employer = Employer.objects.get(id=employer_id)
        employer.user = user
        employer.save()
        send_email(title='', text=f'Ваш логин на uzncd.com: {request.data.get("username")}\nВаш пароль: {request.data.get("password")}', emails=[employer.email, ])
        # send_sms(text=f'your username: {request.data.get("username")}\nyour password: {request.data.get("password")}', number=employer.phone)
        return Response(status=200)


class EmployerEmployeeMakeBusy(APIView):
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


class EmployerRequestDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        EmployerEmployeeRequest.objects.filter(id__in=p_ids).delete()
        return Response()


class EmployersRequestDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data.get('ids')
        p_ids = []
        for i in ids.split(','):
            if i.isdigit():
                p_ids.append(int(i))
        EmployerEmployeeRequest.objects.filter(employer_id__in=p_ids).delete()
        return Response()
