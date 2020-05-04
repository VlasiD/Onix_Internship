from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from locations.models import Country, City


def home(request):
    return render(request, 'locations/home.html')


@login_required(login_url='login/')
def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'locations/countries_list.html', {'countries': countries})


@login_required(login_url='login/')
def cities_list(request, name):
    cities = City.objects.filter(country__name=name)
    return render(request, 'locations/cities_list.html', {'cities': cities})


@login_required(login_url='login/')
def city(request, name):
    item = City.objects.get(name=name)
    return render(request, 'locations/city.html', {'city': item})


@login_required(login_url='login/')
def delete_city(request, name):
    obj = City.objects.get(name=name)
    obj.delete()
    return redirect('/country={}'.format(obj.country))