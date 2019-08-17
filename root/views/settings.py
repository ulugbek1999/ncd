from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from root.mixins import IsSuperUserMixin


class Settings(IsSuperUserMixin, TemplateView):
    template_name = 'root/settings/main.html'

    def post(self, request):
        current_passwd = request.POST.get('current_passwd')
        new_passwd = request.POST.get('new_passwd')
        new_confirm_passwd = request.POST.get('new_confirm_passwd')
        if not current_passwd:
            return JsonResponse(status=400, data={'error': _('current password is empty')})
        if not new_passwd:
            return JsonResponse(status=400, data={'error': _('new password is empty')})
        if not new_confirm_passwd:
            return JsonResponse(status=400, data={'error': _('New confirm password is empty')})

        if not request.user.check_password(current_passwd):
            return JsonResponse(status=400, data={'error': _('current password is incorrect')})
        elif not new_passwd == new_confirm_passwd:
            return JsonResponse(status=400, data={'error': _('passwords didn`t match')})
        else:
            request.user.set_password(new_passwd)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return JsonResponse(status=200, data={})
