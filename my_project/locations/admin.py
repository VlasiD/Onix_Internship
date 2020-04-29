from django.contrib import admin
from locations.models import Country, City, Symbol


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_filter = ['country']


# add models to admin panel
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Symbol)