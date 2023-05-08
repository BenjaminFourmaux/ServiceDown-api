"""
    Service Down api URL Configuration
    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/2.2/topics/http/urls/
    Examples:
        Function views
            1. Add an import:  from my_app import views
            2. Add a URL to urlpatterns:  path('', views.home, name='home')
        Class-based views
            1. Add an import:  from other_app.views import Home
            2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
        Including another URLconf
            1. Import the include() function: from django.urls import include, path
            2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from api.views import TestViewSet, CountriesViewSet, ServicesViewSet, ReportsViewSet, SearchViewSet, StatusViewSet
from django.urls import path, re_path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Service Down API",
        default_version='v1',
        description="Get service status information in real-time",
        contact=openapi.Contact(email="contact@service-down.net"),
    ),
    public=True,
)
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

router = DefaultRouter(trailing_slash=False)

# Route register
router.register('test', TestViewSet, basename='pingViewSet')
router.register('country', CountriesViewSet, basename='countriesViewSet')
router.register('service', ServicesViewSet, basename='servicesViewSet')
router.register('report', ReportsViewSet, basename='reportsViewSet')
router.register('search', SearchViewSet, basename='searchViewSet')
router.register('status', StatusViewSet, basename='statusViewSet')

urlpatterns = [
    re_path('', include(router.urls)),
    re_path(r'^favicon.ico$', favicon_view)
]
