from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('countries', views.countries_list, name='countries_list'),
    path('countries/new', views.create_country, name='create_country'),
    path('country/edit=<int:id>', views.edit_country, name='edit_country'),
    path('country=<int:id>/', views.cities_list, name='cities_list'),
    path('city/new', views.create_city, name='create_city'),
    path('city/edit=<int:id>', views.edit_city, name='edit_city'),
    path('city=<int:id>', views.city, name='city'),
    path('delete=<int:id>', views.delete_city, name='delete_city')
]