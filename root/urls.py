from django.urls import path, include

from .views import directory as directory_views
from .views import employee as employee_views
from .views import operator as operator_views
from .views import rating as rating_views
from .views import employer as employer_views
from .views import templates as template_views
from .views import settings as settings_views


template_patterns = [
    path('list/', template_views.TemplateList.as_view(), name='root.template.list'),
    # path('send-message/', template_views.SendSMSEmail.as_view(), name='root.template.send_message'),
    path('history/', template_views.TemplateHistoryList.as_view(), name='root.template.history'),
    path('history-detail/<int:id>/', template_views.TemplateHistoryDetailView.as_view(), name='root.template.history-detail'),
    path('detail/<int:id>/', template_views.TemplateDetailView.as_view(), name='root.template.detail'),
]

settings_patterns = [
    path('', settings_views.Settings.as_view(), name='root.settings'),
]

employee_patterns = [
    path('operator/1/<int:id>/', employee_views.EmployeeUpdateOP1.as_view(), name='root.employee.update.1'),
    path('operator/2/<int:id>/', employee_views.EmployeeUpdateOP2.as_view(), name='root.employee.update.2'),
    path('operator/3/<int:id>/', employee_views.EmployeeUpdateOP3.as_view(), name='root.employee.update.3'),
    path('operator/4/<int:id>/', employee_views.EmployeeUpdateOP4.as_view(), name='root.employee.update.4'),

    path('translation-1/<int:id>/', employee_views.EmployeeTranslation1.as_view(), name="root.employee.translation.1"),
    path('translation-3/<int:id>/', employee_views.EmployeeTranslation3.as_view(), name="root.employee.translation.3"),
    path('translation-4/<int:id>/', employee_views.EmployeeTranslation4.as_view(), name="root.employee.translation.4"),

    path('statistics/', employee_views.EmployeeStatistics.as_view(), name="root.employee.statistics"),

    path('changed/', employee_views.ChangedEmployeesListView.as_view(), name="root.employee.changed"),
    path('changed/<int:id>/', employee_views.ChangedEmployeeDetailView.as_view(), name="root.employee.changed.detail"),
    # path('export/xls/', employee_views.EmployeeXLSDownload.as_view(), name="root.employee.export.xls"),

    path('<int:id>/export/pdf', employee_views.EmployeeDetailExportPDF.as_view(), name='root.employee.export.pdf'),
    path('<int:id>/', employee_views.EmployeeDetail.as_view(), name='root.employee.detail'),
    path('', employee_views.Employees.as_view(), name='root.employee.list'),
]

rating_patterns = [
    path('', rating_views.Ratings.as_view(), name="root.rating.list")
]

directory_patterns = [
    # list
    path('country/list/', directory_views.CountryListView.as_view(), name='root.directory.country.list'),
    path('city/list/', directory_views.CityListView.as_view(), name='root.directory.city.list'),
    path('district/list/', directory_views.DistrictListView.as_view(), name='root.directory.district.list'),
    path('language/list/', directory_views.LanguageListView.as_view(), name='root.directory.language.list'),
    path('education/list/', directory_views.EducationTypeListView.as_view(), name='root.directory.education.list'),
    # create
    path('country/create/', directory_views.CountryCreateTemplateView.as_view(), name='root.directory.country.create'),
    path('city/create/', directory_views.CityCreateTemplateView.as_view(), name='root.directory.city.create'),
    path('district/create/', directory_views.DistrictCreateTemplateView.as_view(), name='root.directory.district.create'),
    path('language/create/', directory_views.LanguageCreateTemplateView.as_view(), name='root.directory.language.create'),
    path('education/create/', directory_views.EducationTypeCreateTemplateView.as_view(), name='root.directory.education.create'),
    # detail
    path('country/detail/<int:id>/', directory_views.CountryDetailView.as_view(), name='root.directory.country.detail'),
    path('city/detail/<int:id>/', directory_views.CityDetailView.as_view(), name='root.directory.city.detail'),
    path('district/detail/<int:id>/', directory_views.DistrictDetailView.as_view(), name='root.directory.district.detail'),
    path('language/detail/<int:id>/', directory_views.LanguageDetailView.as_view(), name='root.directory.language.detail'),
    path('education/detail/<int:id>/', directory_views.EducationTypeDetailView.as_view(), name='root.directory.education.detail'),
]

operator_patterns = [
    path('groups/', operator_views.OperatorGroups.as_view(), name='root.operator.group.list'),
    path('groups/create/', operator_views.OperatorGroupCreate.as_view(), name='root.operator.group.create'),
    path('groups/<int:id>/', operator_views.OperatorGroupDetail.as_view(), name='root.operator.group.detail'),

    path('create/', operator_views.OperatorCreate.as_view(), name='root.operator.create'),
    path('<int:id>/', operator_views.OperatorDetail.as_view(), name='root.operator.detail'),
    path('', operator_views.Operators.as_view(), name='root.operator.list'),
]

employer_patterns = [
    path('<int:id>/', employer_views.EmployerDetail.as_view(), name='root.employer.detail'),
    path('create/', employer_views.EmployerCreate.as_view(), name='root.employer.create'),
    path('', employer_views.Employers.as_view(), name='root.employer.list'),
]

employer_bookmarks = [
    path('employer/<int:id>/bookmarks/', employer_views.EmployerBookmarks.as_view(), name='root.employer.bookmarks'),
    path('employer/bookmarks/<int:id>/', employer_views.EmployerBookmark.as_view(), name='root.employer.bookmark'),
    path('employers/', employer_views.EmployersBookmark.as_view(), name='root.employers.bookmark'),
]

core_patterns = [
    path('employer/<int:id>/bookmarks/', employer_views.EmployerBookmarks.as_view(), name='root.employer.bookmarks'),
]

urlpatterns = [
    path('employees/', include(employee_patterns)),
    path('operators/', include(operator_patterns)),
    path('employers/', include(employer_patterns)),
    path('employer-bookmark/', include(employer_bookmarks)),
    path('ratings/', include(rating_patterns)),
    path('directory/', include(directory_patterns)),
    path('templates/', include(template_patterns)),
    path('settings/', include(settings_patterns)),
]
