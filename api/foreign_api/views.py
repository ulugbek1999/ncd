import datetime

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.foreign_api.serializers import UserSerializer

#
# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
from employee.model.employee import Employee
from utils.mail import send_email
from utils.sms import send_sms


class UserCreateAPIView(APIView):
    def post(self, request):
        emp_id = request.POST.get("emp_id")
        try:
            emp = Employee.objects.get(id=emp_id)
            user = User()
            if not emp.username == "":
                user.username = emp.username
            else:
                user.username = emp.passport_serial.replace(" ", "")
            passwd = str(int(datetime.datetime.now().timestamp()))
            user.set_password(passwd)
            user.save()
            emp.user = user
            emp.save()
            if emp.send_sms:
                send_sms(emp.phone, f"Ваш логин на uzncd.com: {emp.user.username}\nВаш пароль: {passwd}\nПодпишитесь на наш телеграм канал https://t.me/ncdxba, чтобы следить за новостями.\nOOO \"Taraqqiyot Milliy Markazi Xususiy Bandlik Agentligi\"")
            if emp.send_email and emp.email:
                print(emp.email)
                send_email(
                    title='uzncd.com',
                    text=f"<b>Ваш логин на uzncd.com</b>: {emp.user.username}\n<b>Ваш пароль</b>: {passwd}\nПодпишитесь на наш телеграм канал https://t.me/ncdxba, чтобы следить за новостями.\nOOO \"Taraqqiyot Milliy Markazi Xususiy Bandlik Agentligi\"",
                    emails=[emp.email]
                )
        except Employee.DoesNotExist:
            print("pass")
        return Response()
