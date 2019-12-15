import datetime
from django.db import transaction
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
from employer.models import Employer, EmployerEmployeeRequest, EmployerFile
from employee.model.employee import Employee
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner, IsEmployer, IsEmployee
import os

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
            employee = Employee.objects.get(user=request.user)
            id = employee.id
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

class EmployeeRegisterAPIView(APIView):
    permission_classes = (AllowAny, )

    @transaction.atomic
    def post(self, request):
        username, password = request.data.get("username"), request.data.get("password")
        fullname, email = request.data.get("fullname"), request.data.get("email")
        passport_serial, gender = request.data.get("passport_serial"), request.data.get("gender")
        date_of_issue, expiry_date = request.data.get("date_of_issue"), request.data.get("expiry_date")
        phone, tin = request.data.get("phone"), request.data.get("tin")
        place_of_recidence = request.data.get("place_of_recidence")
        date_of_birth, place_of_birth = request.data.get("date_of_birth"), request.data.get("place_of_birth")
        # print(date_of_birth)
        try:
            user = User(username=username)
            user.set_password(password)
        except Exception as e:
            return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        try:

            employee = Employee(
                full_name_en=fullname,
                email=email,
                passport_serial=passport_serial,
                gender=gender,
                passport_given_date=date_of_issue,
                passport_expires=expiry_date,
                phone=phone,
                inn=tin,
                birth_date=date_of_birth,
                living_address_ru=place_of_recidence,
                birth_place_ru=place_of_birth
            )
            if request.FILES.getlist('file'):
                print(True)
                for i in request.FILES.getlist('file'):
                    employee.photo_1 = i
            user.save()
            employee.user = user
            employee.save()
        except Exception as e:
            if "username" in str(e):
                return Response("Username already exists!", status=HTTP_400_BAD_REQUEST)
            elif "email" in str(e):
                return Response("Email already exists!", status=HTTP_400_BAD_REQUEST)
            elif "passport_serial" in str(e):
                return Response("Passport serial already exists!", status=HTTP_400_BAD_REQUEST)
            else:
                print(e)
                return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        return Response("Successfully registered!", status=HTTP_200_OK)

class EmployeeDeletePhotoAPIView(APIView):
    permission_classes = (IsAuthenticated, IsEmployee, )

    def delete(self, request, photo):
        employee = request.user.employee
        if photo == "photo_1":
            deleteFile(employee.photo_1)
            employee.photo_1 = None
        elif photo == "photo_2":
            deleteFile(employee.photo_2)
            employee.photo_2 = None
        elif photo == "photo_3":
            deleteFile(employee.photo_3)
            employee.photo_3 = None
        elif photo == "photo_4":
            deleteFile(employee.photo_4)
            employee.photo_4 = None
        else:
            return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        try:
            employee.save()
        except:
            return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        return Response("Successfully deleted!", status=HTTP_200_OK)

class EmployeeUpdatePhotoAPIView(APIView):
    permission_classes = (IsOwner, IsEmployee, )

    def put(self, request):
        employee = request.user.employee
        try:
            if request.data.get("photo_1"):
                print(True)
                if employee.photo_1:
                    deleteFile(employee.photo_1)
                    employee.photo_1 = None
                employee.photo_1 = request.data.get("photo_1")
                employee.save()
                return Response(employee.photo_1.url, status=HTTP_200_OK)
            elif request.data.get("photo_2"):
                if employee.photo_2:
                    deleteFile(employee.photo_2)
                    employee.photo_2 = None
                employee.photo_2 = request.data.get("photo_2")
                employee.save()
                return Response(employee.photo_2.url, status=HTTP_200_OK)
            elif request.data.get("photo_3"):
                if employee.photo_3:
                    deleteFile(employee.photo_3)
                    employee.photo_3 = None
                employee.photo_3 = request.data.get("photo_3")
                employee.save()
                return Response(employee.photo_3.url, status=HTTP_200_OK)
            elif request.data.get("photo_4"):
                if employee.photo_4:
                    deleteFile(employee.photo_4)
                    employee.photo_4 = None
                employee.photo_4 = request.data.get("photo_4")
                employee.save()
                return Response(employee.photo_4.url, status=HTTP_200_OK)
            else:
                return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)
        return Response("Something went wrong!", status=HTTP_400_BAD_REQUEST)


def deleteFile(photo):
    if photo:
        if os.path.isfile(photo.path):
            os.remove(photo.path)