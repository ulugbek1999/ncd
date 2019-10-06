from django.contrib import admin

from .models import Employer, EmployerEmployee, EmployerFile, EmployerEmployeeRequest

admin.site.register(Employer)
admin.site.register(EmployerEmployeeRequest)
admin.site.register(EmployerFile)
admin.site.register(EmployerEmployee)
