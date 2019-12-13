from django.urls import path

from api.foreign_api.views import UserCreateAPIView, VisitorsGsheet, VisitorsMailingList, RegisterEmployer
from api.foreign_api.views import Authenticate, GetUserInformation, GetUser, ChangeUserPassword

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view()),
    path('visitors/gsheet/', VisitorsGsheet.as_view()),
    path('visitors/mailing-list/', VisitorsMailingList.as_view()),
    path('register/employer/', RegisterEmployer.as_view()),
    path('authenticate/user/', Authenticate.as_view()),
    path('get/user/', GetUser.as_view()),
    path('get/user/information/<int:id>', GetUserInformation.as_view()),
    path('change/password/<int:id>', ChangeUserPassword.as_view()),
]
