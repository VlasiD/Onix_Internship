from django.utils.deprecation import MiddlewareMixin
from locations.models import Country


class CountriesDisplaying(MiddlewareMixin):
    def process_request(self, request):
        countries_list = Country.objects.all()
        request.countries_list = countries_list
