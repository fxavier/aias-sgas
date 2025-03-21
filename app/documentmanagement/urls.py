from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, DocumentTypeViewSet

router = DefaultRouter()

router.register(r'documents', DocumentViewSet)
router.register(r'document-types', DocumentTypeViewSet)

app_name = 'documentmanagement'

urlpatterns = [
    path('', include(router.urls)),
]
