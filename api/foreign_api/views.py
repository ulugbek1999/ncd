import datetime

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND
from django.utils import timezone
from psycopg2.errorcodes import UNIQUE_VIOLATION
from mail.models import MailingList
from api.foreign_api.serializers import UserSerializer, EmployerRequestCreateSerializer
from django.db.utils import IntegrityError
import json
from employer.models import Employer, EmployerEmployeeRequest
from employee.model.employee import Employee
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner, IsEmployer

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


class RegisterEmployer(CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployerRequestCreateSerializer


class Authenticate(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data

        # Checking whether the user exists
        try:
            user = User.objects.get(username=data.get("username"))
        except User.DoesNotExist:
            return Response("Bad credentials!", status=status.HTTP_406_NOT_ACCEPTABLE)
        password_matches = user.check_password(data.get("password"))
        is_employer = hasattr(user, "employer")
        if password_matches:
                # Generating JSON web token
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = {
                "token": token,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response("Bad credentials!", status=status.HTTP_406_NOT_ACCEPTABLE)

class GetUser(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        is_employer = hasattr(request.user, "employer")
        role = ""
        id = 0
        if not is_employer:
            id = request.user.employee.id
            role = "employee"
        else:
            id = request.user.employer.id
            role = "employer"
        response = {
            "user": {
                "id": id,
                "username": request.user.username,
                "role": role
            }
        }
        return Response(response, status=status.HTTP_200_OK)


class GetUserInformation(RetrieveAPIView):
    queryset = Employer.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )
    lookup_url_kwarg = "id"
    serializer_class = EmployerRequestCreateSerializer

class ChangeUserPassword(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, id):
        print(request.headers)
        request_user = request.user
        if hasattr(request_user, "employer"):
            employer = Employer.objects.get(pk=id)
            if employer.user != request_user:
                return Response("You have not enough privileges to change this data!", status=status.HTTP_403_FORBIDDEN)
            else:
                if employer.user.check_password(request.data.get("old_password")):
                    employer.user.set_password(request.data.get("new_password"))
                    employer.user.save()
                    return Response("Successfully changed!", status=status.HTTP_200_OK)
                else:
                    return Response("Old password is wrong!", status=status.HTTP_406_NOT_ACCEPTABLE)
        elif hasattr(request_user, "employee"):
            employee = Employee.objects.get(pk=id)
            if employee.user != request_user:
                return Response("You have not enough privileges to change this data!", status=status.HTTP_403_FORBIDDEN)
            else:
                if employee.user.check_password(request.data.get("old_password")):
                    employee.user.set_password(request.data.get("new_password"))
                    employee.user.save()
                    return Response("Successfully changed!", status=status.HTTP_200_OK)
                else:
                    return Response("Old password is wrong!", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response("Something went wrong!", status=status.HTTP_400_BAD_REQUEST)

class EmployAPIView(APIView):
    permission_classes = (IsAuthenticated, IsEmployer, )

    def post(self, request):
        employee_id = request.data.get("employee_id")
        try:
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return Response("Oops... Employee does not exist!", status=HTTP_400_BAD_REQUEST)
        try:
            employer = Employer.objects.get(user=request.user)
        except expression as identifier:
            return Response("Oops... Something went wrong!", status=HTTP_400_BAD_REQUEST)
        p, _ = EmployerEmployeeRequest.objects.get_or_create(employer=employer, contract_type=2)
        p.employees.add(employee.id)
        try:
            p.save()
        except expression as identifier:
            return Response(expression, status=HTTP_400_BAD_REQUEST)
        return Response("Successfully added!", status=HTTP_200_OK)

class EmployeeRequestDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated, IsEmployer, )

    def delete(self, request, id):
        try:
            employee = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response("Employee not found!", status=HTTP_404_NOT_FOUND)
        employer_request = EmployerEmployeeRequest.objects.filter(employer=request.user.employer)
        if employer_request.count() == 1:
            try:
                p = employer_request[0]
                e = p.employees.get(pk=id)
                p.employees.remove(e)
                p.save()
            except Employee.DoesNotExist:
                return Response("Employee has already been deleted!", status=HTTP_400_BAD_REQUEST)
            except:
                print(True)
                return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        else:
            return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        return Response("Successfully deleted!", status=HTTP_200_OK)
