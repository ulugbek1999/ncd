from rest_framework.views import APIView
from django.contrib.auth.models import User
from employer.models import Employer


class Create(APIView):
    def post(self, request):
        first_name = request.POST.get('first_name')
