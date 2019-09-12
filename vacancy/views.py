from django.views.generic import ListView, DetailView
from vacancy.models import VacancyRequest
from employee.model.employee import Employee
from pure_pagination import PaginationMixin
from root.mixins import IsSuperUserMixin
from django.db.models import Q


class VacancyRequestListView(IsSuperUserMixin, PaginationMixin, ListView):
    template_name = "root/vacancy/list.html"
    context_object_name = "vr"
    queryset = VacancyRequest.objects.all()
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET
        fullname = data.get("fullname")
        vacancy = data.get("vacancy_name")
        if fullname:
            qs = qs.filter(
                Q(employee__full_name_ru__icontains=fullname) |
                Q(employee__full_name_en__icontains=fullname)
            )
        if vacancy:
            print(vacancy)
            qs = qs.filter(
                Q(vacancy__title_en__icontains=vacancy) |
                Q(vacancy__title_ru__icontains=vacancy) |
                Q(vacancy__title_uz__icontains=vacancy) |
                Q(vacancy__title_kz__icontains=vacancy)
            )
        return qs

class VacancyRequestDetailView(IsSuperUserMixin, DetailView):
    model = VacancyRequest
    template_name = 'root/vacancy/detail.html'
    context_object_name = 'vacancy_request'
    