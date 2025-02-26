import graphene
from graphene import Int, String, Field, List
from graphene_django import DjangoObjectType
from .models import WastManagement

# -------------------------
# Graphene Object Type
# -------------------------

class WastManagementNode(DjangoObjectType):
    class Meta:
        model = WastManagement
        fields = '__all__'

# -------------------------
# Queries
# -------------------------

class Query(graphene.ObjectType):
    all_wast_managements = List(WastManagementNode)
    wast_management = Field(WastManagementNode, id=Int(required=True))

    def resolve_all_wast_managements(root, info):
        return WastManagement.objects.all()

    def resolve_wast_management(root, info, id):
        try:
            return WastManagement.objects.get(pk=id)
        except WastManagement.DoesNotExist:
            return None

# -------------------------
# Mutations
# -------------------------

class CreateWastManagement(graphene.Mutation):
    class Arguments:
        waste_route = String(required=True)
        labelling = String(required=True)
        storage = String(required=True)
        transportation_company_method = String(required=True)
        disposal_company = String(required=True)
        special_instructions = String(required=True)

    wast_management = Field(WastManagementNode)

    def mutate(self, info, waste_route, labelling, storage, transportation_company_method, disposal_company, special_instructions):
        wm = WastManagement.objects.create(
            waste_route=waste_route,
            labelling=labelling,
            storage=storage,
            transportation_company_method=transportation_company_method,
            disposal_company=disposal_company,
            special_instructions=special_instructions
        )
        return CreateWastManagement(wast_management=wm)

class UpdateWastManagement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        waste_route = String()
        labelling = String()
        storage = String()
        transportation_company_method = String()
        disposal_company = String()
        special_instructions = String()

    wast_management = Field(WastManagementNode)

    def mutate(self, info, id, **kwargs):
        try:
            wm = WastManagement.objects.get(pk=id)
        except WastManagement.DoesNotExist:
            raise Exception("WastManagement not found")
        for key, value in kwargs.items():
            setattr(wm, key, value)
        wm.save()
        return UpdateWastManagement(wast_management=wm)

class DeleteWastManagement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            wm = WastManagement.objects.get(pk=id)
        except WastManagement.DoesNotExist:
            raise Exception("WastManagement not found")
        wm.delete()
        return DeleteWastManagement(ok=True)

# -------------------------
# Root Mutation and Schema
# -------------------------

class Mutation(graphene.ObjectType):
    create_wast_management = CreateWastManagement.Field()
    update_wast_management = UpdateWastManagement.Field()
    delete_wast_management = DeleteWastManagement.Field()

class PollutionPreventionStatus(graphene.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

schema = graphene.Schema(query=Query, mutation=Mutation)
