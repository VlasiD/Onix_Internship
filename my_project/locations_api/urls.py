from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from locations_api import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('country/', views.CountryListApiView.as_view()),
    path('country/<int:pk>', views.CountryApiView.as_view()),
    path('country/create/', views.CountryCreateApiView.as_view()),
    path('city/', views.CityListApiView.as_view()),
    path('login/', views.authenticate_user),
    path('register/', views.CreateUserAPIView.as_view()),
    path(r'token/', TokenObtainPairView.as_view()),
    path(r'token/refresh/', TokenRefreshView.as_view()),
    # path('google/', TemplateView.as_view(template_name="registration/google_login.html")),
    path('google/', views.GoogleView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

