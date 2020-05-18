from rest_framework.serializers import ModelSerializer
from locations.models import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'description']