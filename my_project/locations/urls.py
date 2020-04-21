from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:route>', views.display_route, name='route'),
]