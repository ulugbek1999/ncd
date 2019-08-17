from django.urls import path, include

from . import views
from .employee import views as emp_views


partner_patterns = [
    path("update/<int:id>/", views.PartnerUpdate.as_view(), name="admin.api.partner.update")
]

# good
translate_patterns = [
    path('employee/1/<int:id>/', emp_views.EmployeeTranslate1UpdateView.as_view(), name='root.api.employee.translate.1'),
    path('employee/3/education/<int:id>/', emp_views.EducationTranslateUpdate.as_view(), name='root.api.employee.translate.3.education'),
    path('employee/3/army/<int:id>/', emp_views.ArmyTranslateUpdate.as_view(), name='root.api.employee.translate.3.army'),
    path('employee/3/relative/<int:id>/', emp_views.RelativeTranslateUpdate.as_view(), name='root.api.employee.translate.3.relative'),
    path('employee/3/experience/<int:id>/', emp_views.ExperienceTranslateUpdate.as_view(), name='root.api.employee.translate.3.experience'),
    path('employee/3/reward/<int:id>/', emp_views.RewardTranslateUpdate.as_view(), name='root.api.employee.translate.3.reward'),
    path('employee/4/<int:id>/', emp_views.EmployeeTranslate4UpdateView.as_view(), name='root.api.employee.translate.4'),
]

employee_pattern = [
    path('update/1/<int:id>/', views.AdminEmployeeUpdate1.as_view(), name="root.api.employee.update.1"),
    path('update/2/<int:id>/', views.AdminEmployeeUpdate2.as_view(), name="root.api.employee.update.2"),
    path('update/3/education/<int:emp_id>/', views.AdminEmployeeUpdate3Education.as_view(), name="root.api.employee.update.3.education"),
    path('update/3/army/<int:emp_id>/', views.AdminEmployeeUpdate3Army.as_view(), name="root.api.employee.update.3.army"),
    path('update/3/language/<int:emp_id>/', views.AdminEmployeeUpdate3Language.as_view(), name="root.api.employee.update.3.language"),
    path('update/3/family/<int:emp_id>/', views.AdminEmployeeUpdate3Family.as_view(), name="root.api.employee.update.3.family"),
    path('update/3/relative/<int:emp_id>/', views.AdminEmployeeUpdate3Relative.as_view(), name="root.api.employee.update.3.relative"),
    path('update/3/experience/<int:emp_id>/', views.AdminEmployeeUpdate3Experience.as_view(), name="root.api.employee.update.3.experience"),
    path('update/3/reward/<int:emp_id>/', views.AdminEmployeeUpdate3Reward.as_view(), name="root.api.employee.update.3.reward"),
    path('update/4/<int:id>/', views.AdminEmployeeUpdate4.as_view(), name="root.api.employee.update.4"),

]

# not good
urlpatterns = [
    path('translate/', include(translate_patterns)),
    path('employee/', include(employee_pattern)),
    path('operator/update/<int:id>/', views.OperatorUpdate.as_view(), name="root.api.operator.update"),
    path('operator/create/', views.OperatorCreate.as_view(), name="root.api.operator.create"),
    path('group/create/', views.GroupCreate.as_view(), name="root.api.group.create"),
    path('group/update/<int:id>/', views.GroupUpdate.as_view(), name="root.api.group.update"),
    path("parnters/", include(partner_patterns)),
]
