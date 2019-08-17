from django.contrib import admin

from .models import Operator, OperatorGroup, RegisterNumber

admin.site.register(Operator)
admin.site.register(OperatorGroup)
admin.site.register(RegisterNumber)
