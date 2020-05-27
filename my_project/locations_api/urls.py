from django.urls import path, include
from locations_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cities', views.CitiesViewSet, basename='cities')

urlpatterns = [
    path('countries/', views.CountriesListView.as_view()),
    path('countries/<int:pk>', views.CountryView.as_view()),
    path('countries/create', views.CountryCreateView.as_view()),
    path('', include(router.urls))
]

