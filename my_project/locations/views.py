from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from locations.models import Country, City, Symbol
from .forms import CountryForm, CityForm


def home(request):
    return render(request, 'locations/home.html')


@login_required(login_url='login/')
def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'locations/countries_list.html', {'countries': countries})


@login_required(login_url='login/')
def cities_list(request, id):
    country = Country.objects.get(id=id)
    return render(request, 'locations/cities_list.html', {'country': country})


@login_required(login_url='login/')
def city(request, id):
    item = City.objects.get(id=id)
    return render(request, 'locations/city.html', {'city': item})


@login_required(login_url='login/')
def delete_city(request, id):
    obj = City.objects.get(id=id)
    obj.delete()
    return redirect('/country={}'.format(obj.country.id))


@login_required()
def create_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            flag = Symbol.objects.create(image=form.cleaned_data['flag'])
            new_country = form.save(commit=False)
            new_country.flag = flag
            new_country.save()
            return redirect('/countries')
    else:
        form = CountryForm()
        return render(request, 'locations/create_country.html', context={'form': form})


@login_required()
def edit_country(request, id):
    country = Country.objects.get(id=id)
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('/countries')
    else:
        form = CountryForm(instance=country)
        return render(request, 'locations/edit_country.html', context={'form': form})


@login_required()
def create_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.save()
            return redirect('/city={}'.format(new_city.id))
    else:
        form = CityForm()
        return render(request, 'locations/create_city.html', context={'form': form})


@login_required()
def edit_city(request, id):
    city = City.objects.get(id=id)
    if request.method == 'POST':
        form = CityForm(data=request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('/city={}'.format(city.id))
    else:
        form = CityForm(instance=city)
        return render(request, 'locations/edit_city.html', context={'form': form})


