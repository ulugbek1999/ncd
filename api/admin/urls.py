from django.urls import path, include

app_name = 'admin'


urlpatterns = [
    path('directory/', include('api.admin.directory.urls')),
    path('employee/', include('api.admin.employee.urls')),
    path('employer/', include('api.admin.employer.urls')),
    path('operator/', include('api.admin.operator.urls')),
    path('template/', include('api.admin.message_template.urls')),
]
