import graphene
from graphene import Date, Int, String, Field, List
from graphene_django import DjangoObjectType
from .models import WasteTransferLog

# -------------------------
# Graphene Object Type
# -------------------------

class WasteTransferLogNode(DjangoObjectType):
    class Meta:
        model = WasteTransferLog
        fields = '__all__'

# -------------------------
# Queries
# -------------------------

class Query(graphene.ObjectType):
    all_waste_transfer_logs = List(WasteTransferLogNode)
    waste_transfer_log = Field(WasteTransferLogNode, id=Int(required=True))

    def resolve_all_waste_transfer_logs(root, info):
        return WasteTransferLog.objects.all()

    def resolve_waste_transfer_log(root, info, id):
        try:
            return WasteTransferLog.objects.get(pk=id)
        except WasteTransferLog.DoesNotExist:
            return None

# -------------------------
# Mutations
# -------------------------

class CreateWasteTransferLog(graphene.Mutation):
    class Arguments:
        waste_type = String(required=True)
        how_is_waste_contained = String(required=True)
        how_much_waste = Int(required=True)
        reference_number = String(required=True)
        date_of_removal = Date(required=True)
        transfer_company = String(required=True)
        special_instructions = String(required=True)

    waste_transfer_log = Field(WasteTransferLogNode)

    def mutate(self, info, waste_type, how_is_waste_contained, how_much_waste,
               reference_number, date_of_removal, transfer_company, special_instructions):
        log = WasteTransferLog.objects.create(
            waste_type=waste_type,
            how_is_waste_contained=how_is_waste_contained,
            how_much_waste=how_much_waste,
            reference_number=reference_number,
            date_of_removal=date_of_removal,
            transfer_company=transfer_company,
            special_instructions=special_instructions,
        )
        return CreateWasteTransferLog(waste_transfer_log=log)

class UpdateWasteTransferLog(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        waste_type = String()
        how_is_waste_contained = String()
        how_much_waste = Int()
        reference_number = String()
        date_of_removal = Date()
        transfer_company = String()
        special_instructions = String()

    waste_transfer_log = Field(WasteTransferLogNode)

    def mutate(self, info, id, **kwargs):
        try:
            log = WasteTransferLog.objects.get(pk=id)
        except WasteTransferLog.DoesNotExist:
            raise Exception("WasteTransferLog not found")
        for key, value in kwargs.items():
            setattr(log, key, value)
        log.save()
        return UpdateWasteTransferLog(waste_transfer_log=log)

class DeleteWasteTransferLog(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            log = WasteTransferLog.objects.get(pk=id)
        except WasteTransferLog.DoesNotExist:
            raise Exception("WasteTransferLog not found")
        log.delete()
        return DeleteWasteTransferLog(ok=True)

# -------------------------
# Root Mutation and Schema
# -------------------------

class Mutation(graphene.ObjectType):
    create_waste_transfer_log = CreateWasteTransferLog.Field()
    update_waste_transfer_log = UpdateWasteTransferLog.Field()
    delete_waste_transfer_log = DeleteWasteTransferLog.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
