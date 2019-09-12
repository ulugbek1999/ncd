from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from vacancy.models import VacancyRequest
from rest_framework.generics import DestroyAPIView
from utils.sms import send_sms
from utils.mail import send_email

class VacancyRequestDeleteAPIVIew(APIView):
    permission_classes = (IsAdminUser, )

    def delete(self, request):
        del_list = request.data.get('delete_list')
        for d in del_list:
            VacancyRequest.objects.get(id=d).delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class VacancyRequestDestroyAPIView(DestroyAPIView):
    queryset = VacancyRequest.objects.all()
    permission_classes = (IsAdminUser, )

class SendResponseVacancyAPIView(APIView):
    permission_classes = (IsAdminUser, )

    def post(self, request):
        ''' Handles response messages to requests on vacancies '''
        emails = []
        
        # Getting data from request
        title = request.data.get("message").get("title")
        content = request.data.get("message").get("content")
        phone = request.data.get("employee").get("phone")
        email = request.data.get("employee").get("email")
        isSms = request.data.get("types").get("sms")
        isEmail = request.data.get("types").get("email")

        emails.append(email)
        message = title + "\n" + content

        # Respond to the applicant
        if isSms:
            send_sms(phone, message)
        if isEmail:
            send_email(title, content, emails)
        return Response(status=status.HTTP_200_OK)
