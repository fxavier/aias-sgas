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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt
from app.schema import schema  # Import the schema
from app.views import download_file  # Import the view we'll create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('riskmanagement/', include('riskmanagement.urls')),
    path('api/graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
    path('https://ggitxibhsovusmdtfqwt.supabase.co/storage/v1/s3/documents/<str:file_key>', download_file, name='download_file'),  # Add download endpoint
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
