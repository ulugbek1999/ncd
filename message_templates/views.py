from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Template


class MessageTemplateCreate(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        Template.objects.create(title=title, text=text)
        return HttpResponse(status=200)
