from django.urls import path

from api.admin.partner.views import PartnerCreateAPIView, PartnerDeleteAPIView, \
    PartnerCreateAccountAPIView, PartnerEmployeeMakeBusy, PartnerRequestDeleteAPIView,\
    PartnersRequestDeleteAPIView

app_name = 'partner'

urlpatterns = [
    path('create/', PartnerCreateAPIView.as_view(), name='create'),
    path('change-account/<int:partner_id>', PartnerCreateAccountAPIView.as_view(), name='change-account'),
    path('delete/', PartnerDeleteAPIView.as_view(), name='delete'),
    path('partner-employee-request/delete/', PartnerRequestDeleteAPIView.as_view(), name='partner-employee-request-delete'),
    path('employee/make-busy/', PartnerEmployeeMakeBusy.as_view(), name='employee-make-busy'),
    path('request/delete/', PartnersRequestDeleteAPIView.as_view(), name='request-delete'),
]
