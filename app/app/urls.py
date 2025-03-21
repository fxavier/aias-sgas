"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from app.admin import custom_admin_site
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt
from app.schema import schema  # Import the schema
from app.views import download_file  # Import the view we'll create
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from documentmanagement.views import DocumentViewSet, DocumentTypeViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Sistema de gestao ambiental API",
        default_version='v1',
        description="API for managing students, courses, and academic records",
        terms_of_service="https://www.yourschool.com/terms/",
        contact=openapi.Contact(email="contact@yourschool.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('sgas/', custom_admin_site.urls),

    path('riskmanagement/', include('riskmanagement.urls')),
    path('api/graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
    path('https://ggitxibhsovusmdtfqwt.supabase.co/storage/v1/s3/documents/<str:file_key>', download_file, name='download_file'),
    path('api/v1/documentmanagement/', include('documentmanagement.urls')),  # Add download endpoint

    # Swagger UI endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
