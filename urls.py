from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='uzncd API')

api_patterns = [
    path('employee/', include('employee.api.urls')),
    path('root/', include('root.api.urls')),
    path('vacancy/', include('vacancy.api.urls')),
]

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('templates/', include('message_templates.urls')),
    path('admin/', admin.site.urls),
    # path('employee/', include('employee.urls')),
    path('api/', include(api_patterns)),
    path('api-view/', schema_view),

    path('api/v2/', include('api.urls')),
    path('logs/', include('log.urls')),
    path('directory/', include('directory.urls')),
    path('vacancy/', include('vacancy.urls'))
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('root/', include('root.urls')),
    # path('operator/', include('operators.urls')),
)

if settings.DEBUG:
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
