from django.test import TestCase
import smtplib
from email.message import Message

# info@osg.uz
# o123123G!

server = smtplib.SMTP_SSL(host='smtp.mail.ru', port=465)
# server.user = 'admin@mail.uzncd.com'
# server.password = 'u123123D!'
# server.starttls()
res = server.login('admin@uzncd.com', 'u123123D!')
# res = server.login('info@osg.uz', 'o123123G!')
print(res)
m = Message()
m.set_payload('asdadasd')
server.send_message(m, 'admin@uzncd.com', 'mukhammadievf@gmail.com')
