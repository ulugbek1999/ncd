from django.urls import path, include

urlpatterns = [
    path('1/', include('api.operators.operator1.urls')),
    path('2/', include('api.operators.operator2.urls')),
    path('3/', include('api.operators.operator3.urls')),
    path('4/', include('api.operators.operator4.urls')),
]
