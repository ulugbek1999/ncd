from django.urls import path

from . import views

urlpatterns = [
    path('auth/signin/', views.AuthSignin.as_view(), name='auth.signin'),
    path('auth/signout/', views.AuthSignout.as_view(), name='auth.signout'),
    path('', views.Index.as_view(), name='index'),
]
