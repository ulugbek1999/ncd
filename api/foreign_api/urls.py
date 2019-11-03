from django.urls import path

from api.foreign_api.views import UserCreateAPIView, VisitorsGsheet, VisitorsMailingList

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view()),
    path('visitors/gsheet/', VisitorsGsheet.as_view()),
    path('visitors/mailing-list/', VisitorsMailingList.as_view())
]
