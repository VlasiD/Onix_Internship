from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from locations.models import Country, City
from locations_api.serializers import CountrySerializer, CitySerializer
from rest_framework import generics



# ViewSet
class CitiesViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country_id']


# Generics
class CountriesListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryCreateView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


