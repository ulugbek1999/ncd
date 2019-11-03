import datetime

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from django.utils import timezone
from psycopg2.errorcodes import UNIQUE_VIOLATION
from mail.models import MailingList
from api.foreign_api.serializers import UserSerializer
from django.db.utils import IntegrityError

#
# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
from employee.model.employee import Employee
from utils.mail import send_email
from utils.sms import send_sms
from utils.gspread import send_gspread


class UserCreateAPIView(APIView):
    def post(self, request):
        emp_id = request.POST.get("emp_id")
        phone = request.POST.get("phone")

        email = request.POST.get("email")
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
            if phone:
                emp.send_sms = True
                emp.save()
                send_sms(phone, f"Ваш логин на uzncd.com: {emp.user.username}\nВаш пароль: {passwd}\nПодпишитесь на наш телеграм канал https://t.me/ncdxba, чтобы следить за новостями.\nOOO \"Taraqqiyot Milliy Markazi Xususiy Bandlik Agentligi\"")
            if emp.send_email and emp.email:
                send_email(
                    title='uzncd.com',
                    text=f"<b>Ваш логин на uzncd.com</b>: {emp.user.username}\n<b>Ваш пароль</b>: {passwd}\nПодпишитесь на наш телеграм канал https://t.me/ncdxba, чтобы следить за новостями.\nOOO \"Taraqqiyot Milliy Markazi Xususiy Bandlik Agentligi\"",
                    emails=[emp.email]
                )
            if phone and email:
                emp.send_sms = True
                emp.send_email = True
                emp.save()
                send_email(
                    title='uzncd.com',
                    text=f"<b>Ваш логин на uzncd.com</b>: {emp.user.username}\n<b>Ваш пароль</b>: {passwd}\nПодпишитесь на наш телеграм канал https://t.me/ncdxba, чтобы следить за новостями.\nOOO \"Taraqqiyot Milliy Markazi Xususiy Bandlik Agentligi\"",
                    emails=[email]
                )
        except Employee.DoesNotExist:
            pass
        return Response()


class VisitorsGsheet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        name, email = request.data.get("name"), request.data.get("email")
        subject, message = request.data.get("subject"), request.data.get("message")
        location = request.data.get("location")
        if not name:
            return Response("Name cannot be empty!", status=HTTP_400_BAD_REQUEST)
        if not email:
            return Response("Email cannot be empty!", status=HTTP_400_BAD_REQUEST)
        if not subject:
            return Response("Subject cannot be empty!", status=HTTP_400_BAD_REQUEST)
        if not message:
            return Response("Message cannot be empty!", status=HTTP_400_BAD_REQUEST)
        if not location:
            return Response("Location cannot be empty!", status=HTTP_400_BAD_REQUEST)
        date = timezone.now()
        date_str = date.strftime("%H:%M:%S %d.%m.%Y")
        send_gspread([
            name,
            email,
            subject,
            message,
            location,
            date_str
        ])
        return Response("Thank you for your request! We will contact you soon.", status=HTTP_200_OK)

class VisitorsMailingList(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        email, country_code = request.data.get("email"), request.data.get("country_code")
        try:
            MailingList.objects.create(email = email, country_code = country_code)
        except IntegrityError:
            return Response("This email has already been added to the list!", status=HTTP_400_BAD_REQUEST)
        
        return Response("Congratulations! You have successfully subscribed.", status=HTTP_200_OK)