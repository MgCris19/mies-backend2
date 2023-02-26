from django.contrib import admin
from django.urls import path, include, re_path

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BackEnd Application Mies",
        default_version='v1',
        description="comunitarias mies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mies@ug.edu.ec"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

contentPath = "mies"
env = "/dev"
url = contentPath+env

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path(url, include('app.user.router')),
    path(url, include('app.economyActivity.router')),
    path(url, include('app.login.urls')),
    path(url, include('app.entrepreneurShip.router')),
    path(url, include('app.entrepreneur.router')),
    path(url, include('app.entrepreneurcourses.router')),
    path(url, include('app.academic.router')),
    path(url, include('app.course.router')),
    path(url, include('app.bond.router')),
    path(url, include('app.menu.router')),
    path(url, include('app.action.router')),
    path(url, include('app.profile.router')),
    path(url, include('app.logGeneral.router')),
    path(url, include('app.observations.router')),
    path(url, include('app.balancedScoredCard.router')),
]
