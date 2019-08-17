from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/notify/operator2/(?P<room_name>[^/]+)/$', consumers.NotifyOperator2),
]
