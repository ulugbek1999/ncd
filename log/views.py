from django.shortcuts import render
from django.views.generic import ListView

from .models import Log


class Logs(ListView):
    model = Log
    template_name = "root/logs.html"
    context_object_name = "logs"
