from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from operators.models import OperatorGroup, Operator


class OperatorGroupDeleteView(APIView):
    def post(self, request):
        ids = request.POST.get('ids')
        if not ids:
            return Response(status=400)
        ids = [int(i) for i in ids.split(',') if i.isdigit()]
        OperatorGroup.objects.filter(id__in=ids).delete()
        return Response(status=200)


class OperatorDeleteView(APIView):
    def post(self, request):
        ids = request.POST.get('ids')
        if not ids:
            return Response(status=400)
        ids = [int(i) for i in ids.split(',') if i.isdigit()]
        user_ids = [i.user.id for i in Operator.objects.filter(id__in=ids)]
        User.objects.filter(id__in=user_ids).delete()
        return Response(status=200)


class OperatorChangeUsernamePassword(APIView):
    def post(self, request, user_id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            u = User.objects.get(id=user_id)
            if username:
                u.username = username
            if password:
                u.set_password(password)
                update_session_auth_hash(request, u)
            u.save()
        except User.DoesNotExist:
            pass
        return Response()
