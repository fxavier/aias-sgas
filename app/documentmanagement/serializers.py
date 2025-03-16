from rest_framework import serializers
from django.core.files.storage import default_storage
import os
from .models import DocumentType, Document


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    document_type_description = serializers.ReadOnlyField(source='document_type.description')
    created_by_username = serializers.ReadOnlyField(source='created_by.username')
    document_state_display = serializers.ReadOnlyField(source='get_document_state_display')
    document_file = serializers.FileField(write_only=True, required=False)
    remove_document = serializers.BooleanField(write_only=True, required=False)
    
    class Meta:
        model = Document
        fields = [
            'id', 'code', 'creation_date', 'revision_date', 'document_name',
            'document_type', 'document_type_description', 'document_path',
            'document_state', 'document_state_display', 'retention_period',
            'disposal_method', 'observation', 'created_by', 'created_by_username',
            'document_file', 'remove_document'
        ]
        
    def validate(self, attrs):
        # Validate file upload and removal logic
        document_file = attrs.get('document_file')
        remove_document = attrs.get('remove_document')
        
        # Check if both actions are requested
        if document_file and remove_document:
            raise serializers.ValidationError(
                "Cannot both upload a new file and remove the existing file in the same request."
            )
            
        # For new documents, ensure a file is provided
        if not self.instance and not document_file and not self.context.get('partial', False):
            raise serializers.ValidationError(
                "A document file is required when creating a new document."
            )
            
        return attrs
    
    def create(self, validated_data):
        # Extract file-related fields
        document_file = validated_data.pop('document_file', None)
        validated_data.pop('remove_document', None)  # Not needed for create
        
        # Create document instance
        document = Document.objects.create(**validated_data)
        
        # Handle document file upload
        if document_file:
            document.document_path.save(document_file.name, document_file)
            
        return document
    
    def update(self, instance, validated_data):
        # Extract file-related fields
        document_file = validated_data.pop('document_file', None)
        remove_document = validated_data.pop('remove_document', False)
        
        # Update instance with validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Handle file removal
        if remove_document and instance.document_path:
            # Store the path for deletion after save
            old_path = instance.document_path.path if instance.document_path else None
            instance.document_path = None
            
            # Delete the old file if it exists
            if old_path and os.path.isfile(old_path):
                default_storage.delete(old_path)
        
        # Handle file upload
        if document_file:
            # Remove old file if exists
            if instance.document_path:
                old_path = instance.document_path.path if instance.document_path else None
                if old_path and os.path.isfile(old_path):
                    default_storage.delete(old_path)
            
            # Save new file
            instance.document_path.save(document_file.name, document_file)
        
        instance.save()
        return instance