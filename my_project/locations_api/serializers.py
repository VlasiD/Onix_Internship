from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from locations.models import Country, City


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')