import graphene
from graphene_django import DjangoObjectType
from graphene import Date
from graphene_file_upload.scalars import Upload  # enables file uploads
from .models import Document, DocumentType, DocumentState
from users.models import User

# Graphene type for DocumentType model.
class DocumentTypeNode(DjangoObjectType):
    class Meta:
        model = DocumentType
        fields = '__all__'

# Graphene Enum for DocumentState
class DocumentStateEnum(graphene.Enum):
    REVISION = "REVISION"
    INUSE = "INUSE"
    OBSOLETE = "OBSOLETE"

# Graphene type for Document model.
class DocumentNode(DjangoObjectType):
    class Meta:
        model = Document
        fields = '__all__'


# Queries for Document and DocumentType.
class Query(graphene.ObjectType):
    all_documents = graphene.List(DocumentNode)
    document_by_id = graphene.Field(DocumentNode, id=graphene.Int(required=True))
    all_document_types = graphene.List(DocumentTypeNode)
    document_type_by_id = graphene.Field(DocumentTypeNode, id=graphene.Int(required=True))

    def resolve_all_documents(root, info):
        return Document.objects.all()

    def resolve_document_by_id(root, info, id):
        try:
            return Document.objects.get(id=id)
        except Document.DoesNotExist:
            return None

    def resolve_all_document_types(root, info):
        return DocumentType.objects.all()

    def resolve_document_type_by_id(root, info, id):
        try:
            return DocumentType.objects.get(id=id)
        except DocumentType.DoesNotExist:
            return None


# Mutation for creating a new DocumentType.
class CreateDocumentType(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)

    document_type = graphene.Field(DocumentTypeNode)

    def mutate(self, info, description):
        document_type = DocumentType.objects.create(description=description)
        return CreateDocumentType(document_type=document_type)


# Mutation for creating a new Document.
class CreateDocument(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)
        creation_date = Date(required=True)
        revision_date = Date(required=True)
        document_name = graphene.String(required=True)
        document_type_id = graphene.Int(required=True)
        # Use Upload type to handle file uploads
        document_path = Upload(required=True)
        document_state = DocumentStateEnum(required=True)
        retention_period = Date(required=True)
        disposal_method = graphene.String(required=True)
        observation = graphene.String(required=True)
        created_by_id = graphene.Int(required=True)

    document = graphene.Field(DocumentNode)

    def mutate(
        self,
        info,
        code,
        creation_date,
        revision_date,
        document_name,
        document_type_id,
        document_path,
        document_state,
        retention_period,
        disposal_method,
        observation,
        created_by_id,
    ):
        try:
            doc_type = DocumentType.objects.get(id=document_type_id)
        except DocumentType.DoesNotExist:
            raise Exception("DocumentType not found")

        try:
            user = User.objects.get(id=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        
        # Use getattr to handle both enum instances and plain strings.
        state_value = getattr(document_state, "value", document_state)

         # If document_path comes in as a list, take the first element.
        if isinstance(document_path, list):
            document_path = document_path[0]

        # The uploaded file is handled by Django's FileField
        document = Document.objects.create(
            code=code,
            creation_date=creation_date,
            revision_date=revision_date,
            document_name=document_name,
            document_type=doc_type,
            document_path=document_path,
            document_state=state_value,
            retention_period=retention_period,
            disposal_method=disposal_method,
            observation=observation,
            created_by=user,
        )
        return CreateDocument(document=document)


# Mutation for updating an existing Document.
class UpdateDocument(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        code = graphene.String()
        creation_date = Date()
        revision_date = Date()
        document_name = graphene.String()
        document_type_id = graphene.Int()
        # Use Upload type here as well; it's optional for updates.
        document_path = Upload()
        document_state = DocumentStateEnum()
        retention_period = Date()
        disposal_method = graphene.String()
        observation = graphene.String()
        created_by_id = graphene.Int()

    document = graphene.Field(DocumentNode)

    def mutate(self, info, id, **kwargs):
        try:
            document = Document.objects.get(id=id)
        except Document.DoesNotExist:
            raise Exception("Document not found")

        if 'code' in kwargs and kwargs['code'] is not None:
            document.code = kwargs['code']
        if 'creation_date' in kwargs and kwargs['creation_date'] is not None:
            document.creation_date = kwargs['creation_date']
        if 'revision_date' in kwargs and kwargs['revision_date'] is not None:
            document.revision_date = kwargs['revision_date']
        if 'document_name' in kwargs and kwargs['document_name'] is not None:
            document.document_name = kwargs['document_name']
        if 'document_type_id' in kwargs and kwargs['document_type_id'] is not None:
            try:
                document.document_type = DocumentType.objects.get(id=kwargs['document_type_id'])
            except DocumentType.DoesNotExist:
                raise Exception("DocumentType not found")
        if 'document_path' in kwargs and kwargs['document_path'] is not None:
            # Update file field with new uploaded file
            document.document_path = kwargs['document_path']
        if 'document_state' in kwargs and kwargs['document_state'] is not None:
            document.document_state = kwargs['document_state'].value
        if 'retention_period' in kwargs and kwargs['retention_period'] is not None:
            document.retention_period = kwargs['retention_period']
        if 'disposal_method' in kwargs and kwargs['disposal_method'] is not None:
            document.disposal_method = kwargs['disposal_method']
        if 'observation' in kwargs and kwargs['observation'] is not None:
            document.observation = kwargs['observation']
        if 'created_by_id' in kwargs and kwargs['created_by_id'] is not None:
            try:
                document.created_by = User.objects.get(id=kwargs['created_by_id'])
            except User.DoesNotExist:
                raise Exception("User not found")
        document.save()
        return UpdateDocument(document=document)


# Mutation for deleting a Document.
class DeleteDocument(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            document = Document.objects.get(id=id)
        except Document.DoesNotExist:
            raise Exception("Document not found")

        document.delete()
        return DeleteDocument(ok=True)


# Root mutation type.
class Mutation(graphene.ObjectType):
    create_document_type = CreateDocumentType.Field()
    create_document = CreateDocument.Field()
    update_document = UpdateDocument.Field()
    delete_document = DeleteDocument.Field()


# Create the schema.
schema = graphene.Schema(query=Query, mutation=Mutation)
