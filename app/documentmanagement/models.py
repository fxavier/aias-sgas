from django.db import models
from users.models import User

class DocumentType(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
class DocumentState(models.TextChoices):
    REVISION = 'REVISION', 'Revisão'
    INUSE = 'INUSE', 'Em uso'
    OBSOLETE = 'OBSOLETE', 'Obsoleto'
    
class Document(models.Model):
    code = models.CharField(max_length=255)
    creation_date = models.DateField()
    revision_date = models.DateField()
    document_name = models.CharField(max_length=255)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document_path = models.FileField(upload_to='documents/')
    document_state = models.CharField(max_length=50, choices=DocumentState.choices)
    retention_period = models.DateField()
    disposal_method = models.CharField(max_length=255)
    observation = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.document_name
