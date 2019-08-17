from django.contrib import admin

from .models import Partner, PartnerEmployee, PartnerFile, PartnerEmployeeRequest

admin.site.register(Partner)
admin.site.register(PartnerEmployeeRequest)
admin.site.register(PartnerFile)
admin.site.register(PartnerEmployee)
