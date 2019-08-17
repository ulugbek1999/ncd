from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('operators/', include('api.operators.urls')),
    path('admin/', include('api.admin.urls')),
    path('directory/', include('api.directory.urls')),
    path('ncd/', include('api.foreign_api.urls')),
]
