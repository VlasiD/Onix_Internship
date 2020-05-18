from rest_framework.viewsets import ModelViewSet
from locations.models import Country
from locations_api.serializers import CountrySerializer


class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
