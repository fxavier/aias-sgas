from rest_framework import viewsets, filters, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.storage import default_storage
from django.http import FileResponse, Http404
import os

from .models import DocumentType, Document
from .serializers import DocumentTypeSerializer, DocumentSerializer
from .filters import DocumentFilter


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description']
    ordering_fields = ['description']
    ordering = ['description']


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DocumentFilter
    search_fields = ['code', 'document_name', 'observation']
    ordering_fields = [
        'code', 'creation_date', 'revision_date', 'document_name',
        'document_type', 'document_state', 'retention_period'
    ]
    ordering = ['-creation_date']
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    
    def perform_create(self, serializer):
        # Automatically set created_by to the current user
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        """Endpoint to download the document file."""
        document = self.get_object()
        
        if not document.document_path:
            return Response(
                {"detail": "This document has no file attached."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        try:
            file_path = document.document_path.path
            if not os.path.exists(file_path):
                return Response(
                    {"detail": "File not found on storage."},
                    status=status.HTTP_404_NOT_FOUND
                )
                
            # Open the file and create a response
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
            
        except Exception as e:
            return Response(
                {"detail": f"Error retrieving file: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['post'])
    def upload(self, request, pk=None):
        """Dedicated endpoint for file uploads."""
        document = self.get_object()
        
        if 'file' not in request.FILES:
            return Response(
                {"detail": "No file provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        uploaded_file = request.FILES['file']
        
        # Remove old file if exists
        if document.document_path:
            old_path = document.document_path.path
            if os.path.exists(old_path):
                default_storage.delete(old_path)
        
        # Save new file
        document.document_path.save(uploaded_file.name, uploaded_file)
        document.save()
        
        serializer = self.get_serializer(document)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['delete'])
    def remove_file(self, request, pk=None):
        """Dedicated endpoint to remove attached file."""
        document = self.get_object()
        
        if not document.document_path:
            return Response(
                {"detail": "This document has no file to remove."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Store path before clearing it
        old_path = document.document_path.path
        
        # Clear the file field
        document.document_path = None
        document.save()
        
        # Delete the actual file
        if os.path.exists(old_path):
            default_storage.delete(old_path)
            
        return Response(
            {"detail": "File removed successfully."},
            status=status.HTTP_204_NO_CONTENT
        )