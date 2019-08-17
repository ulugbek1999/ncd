from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from pure_pagination.mixins import PaginationMixin

from directory.models import City, District, Country, EducationType
from directory.models import Language
from root.mixins import IsSuperUserMixin


# city
class CityListView(IsSuperUserMixin, PaginationMixin, ListView):
    model = City
    template_name = 'root/directory/city_list.html'
    context_object_name = 'cities'
    paginate_by = 10

    def get_queryset(self):
        qs = City.objects.all()
        name = self.request.GET.get('name')
        if name:
            qs = qs.filter(
                Q(name_ru__icontains=name) |
                Q(name_en__icontains=name)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name:
            context['name'] = name
        return context


# detail
class CityDetailView(IsSuperUserMixin, DetailView):
    model = City
    template_name = 'root/directory/city_detail.html'
    context_object_name = 'city'
    pk_url_kwarg = 'id'


# create template
class CityCreateTemplateView(IsSuperUserMixin, TemplateView):
    template_name = 'root/directory/city_create.html'


# district
# list
class DistrictListView(IsSuperUserMixin, PaginationMixin, ListView):
    model = District
    template_name = 'root/directory/district_list.html'
    context_object_name = 'districts'
    paginate_by = 10

    def get_queryset(self):
        qs = District.objects.all()
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        if name:
            qs = qs.filter(
                Q(name_ru__icontains=name) |
                Q(name_en__icontains=name)
            )
        if city:
            if city.isdigit():
                qs = qs.filter(city__id=city)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        if name:
            context['name'] = name
        if city:
            if city.isdigit():
                context['city_id'] = int(city)
        context['cities'] = City.objects.all()
        return context


# detail
class DistrictDetailView(IsSuperUserMixin, DetailView):
    model = District
    template_name = 'root/directory/district_detail.html'
    context_object_name = 'district'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context


# create template
class DistrictCreateTemplateView(IsSuperUserMixin, TemplateView):
    template_name = 'root/directory/district_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        if name:
            context['name'] = name
        if city:
            context['score'] = city
        context['cities'] = City.objects.all()
        return context


# country
# list
class CountryListView(IsSuperUserMixin, PaginationMixin, ListView):
    model = Country
    template_name = 'root/directory/country_list.html'
    context_object_name = 'countries'
    paginate_by = 10

    def get_queryset(self):
        qs = Country.objects.all()
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            qs = qs.filter(
                Q(name_ru__icontains=name) |
                Q(name_en__icontains=name)
            )
        if score:
            if score.isdigit():
                qs = qs.filter(score=score)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            context['name'] = name
        if score:
            if score.isdigit():
                context['score'] = score
        return context


# detail
class CountryDetailView(IsSuperUserMixin, DetailView):
    model = Country
    template_name = 'root/directory/country_detail.html'
    context_object_name = 'country'
    pk_url_kwarg = 'id'


# create template
class CountryCreateTemplateView(IsSuperUserMixin, TemplateView):
    template_name = 'root/directory/country_create.html'


# language
# list
class LanguageListView(IsSuperUserMixin, PaginationMixin, ListView):
    model = Language
    template_name = 'root/directory/language_list.html'
    context_object_name = 'languages'
    paginate_by = 10

    def get_queryset(self):
        qs = Language.objects.all()
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            qs = qs.filter(
                Q(name_ru__icontains=name) |
                Q(name_en__icontains=name)
            )
        if score:
            if score.isdigit():
                qs = qs.filter(
                    Q(excellent=score) |
                    Q(good=score) |
                    Q(not_bad=score)
                )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            context['name'] = name
        if score:
            context['score'] = score
        return context


# detail
class LanguageDetailView(IsSuperUserMixin, DetailView):
    model = Language
    template_name = 'root/directory/language_detail.html'
    context_object_name = 'language'
    pk_url_kwarg = 'id'


# create template
class LanguageCreateTemplateView(IsSuperUserMixin, TemplateView):
    template_name = 'root/directory/language_create.html'


# education
# list
class EducationTypeListView(IsSuperUserMixin, PaginationMixin, ListView):
    model = EducationType
    template_name = 'root/directory/education_list.html'
    context_object_name = 'educations'
    paginate_by = 10

    def get_queryset(self):
        qs = EducationType.objects.all()
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            qs = qs.filter(
                Q(name_ru__icontains=name) |
                Q(name_en__icontains=name)
            )
        if score:
            if score.isdigit():
                qs = qs.filter(score=score)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        score = self.request.GET.get('score')
        if name:
            context['name'] = name
        if score:
            context['score'] = score
        return context


# detail
class EducationTypeDetailView(IsSuperUserMixin, DetailView):
    model = EducationType
    template_name = 'root/directory/education_detail.html'
    context_object_name = 'education'
    pk_url_kwarg = 'id'


# create template
class EducationTypeCreateTemplateView(IsSuperUserMixin, TemplateView):
    template_name = 'root/directory/education_create.html'
