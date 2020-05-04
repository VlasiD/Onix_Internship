from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('countries', views.countries_list, name='countries_list'),
    path('country=<str:name>/', views.cities_list, name='cities_list'),
    path('city=<str:name>', views.city, name='city'),
    path('delete=<str:name>', views.delete_city, name='delete_city')
]