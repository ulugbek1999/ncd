# from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings


def send_email(title, text, emails):
    msg = EmailMultiAlternatives(title, strip_tags(text), settings.EMAIL_HOST_USER, emails)
    msg.attach_alternative(text, "text/html")
    a = msg.send()
    print(a)
