import graphene
from graphene import Date, Int, String, Field, List
from graphene_django import DjangoObjectType

from .models import StrategicObjective, SpecificObjective

# -------------------------
# Graphene Object Types
# -------------------------

class StrategicObjectiveNode(DjangoObjectType):
    class Meta:
        model = StrategicObjective
        fields = '__all__'

class SpecificObjectiveNode(DjangoObjectType):
    class Meta:
        model = SpecificObjective
        fields = '__all__'

# -------------------------
# Queries
# -------------------------

class Query(graphene.ObjectType):
    all_strategic_objectives = List(StrategicObjectiveNode)
    strategic_objective = Field(StrategicObjectiveNode, id=Int(required=True))
    
    all_specific_objectives = List(SpecificObjectiveNode)
    specific_objective = Field(SpecificObjectiveNode, id=Int(required=True))
    
    def resolve_all_strategic_objectives(root, info):
        return StrategicObjective.objects.all()
    
    def resolve_strategic_objective(root, info, id):
        try:
            return StrategicObjective.objects.get(pk=id)
        except StrategicObjective.DoesNotExist:
            return None
    
    def resolve_all_specific_objectives(root, info):
        return SpecificObjective.objects.all()
    
    def resolve_specific_objective(root, info, id):
        try:
            return SpecificObjective.objects.get(pk=id)
        except SpecificObjective.DoesNotExist:
            return None

# -------------------------
# Mutations for StrategicObjective
# -------------------------

class CreateStrategicObjective(graphene.Mutation):
    class Arguments:
        description = String(required=True)
        goals = String(required=True)
        strategies_for_achievement = String(required=True)
    
    strategic_objective = Field(StrategicObjectiveNode)
    
    def mutate(self, info, description, goals, strategies_for_achievement):
        so = StrategicObjective.objects.create(
            description=description,
            goals=goals,
            strategies_for_achievement=strategies_for_achievement
        )
        return CreateStrategicObjective(strategic_objective=so)

class UpdateStrategicObjective(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        description = String()
        goals = String()
        strategies_for_achievement = String()
    
    strategic_objective = Field(StrategicObjectiveNode)
    
    def mutate(self, info, id, **kwargs):
        try:
            so = StrategicObjective.objects.get(pk=id)
        except StrategicObjective.DoesNotExist:
            raise Exception("StrategicObjective not found")
        for key, value in kwargs.items():
            setattr(so, key, value)
        so.save()
        return UpdateStrategicObjective(strategic_objective=so)

class DeleteStrategicObjective(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            so = StrategicObjective.objects.get(pk=id)
        except StrategicObjective.DoesNotExist:
            raise Exception("StrategicObjective not found")
        so.delete()
        return DeleteStrategicObjective(ok=True)

# -------------------------
# Mutations for SpecificObjective
# -------------------------

class CreateSpecificObjective(graphene.Mutation):
    class Arguments:
        strategic_objective = String(required=True)
        specific_objective = String(required=True)
        actions_for_achievement = String(required=True)
        responsible_person = String(required=True)
        necessary_resources = String(required=True)
        indicator = String(required=True)
        goal = String(required=True)
        monitoring_frequency = String(required=True)
        deadline = Date(required=True)
        observation = String(required=True)
    
    specific_objective_obj = Field(SpecificObjectiveNode)
    
    def mutate(self, info, strategic_objective, specific_objective, actions_for_achievement,
               responsible_person, necessary_resources, indicator, goal,
               monitoring_frequency, deadline, observation):
        so_obj = SpecificObjective.objects.create(
            strategic_objective=strategic_objective,
            specific_objective=specific_objective,
            actions_for_achievement=actions_for_achievement,
            responsible_person=responsible_person,
            necessary_resources=necessary_resources,
            indicator=indicator,
            goal=goal,
            monitoring_frequency=monitoring_frequency,
            deadline=deadline,
            observation=observation
        )
        return CreateSpecificObjective(specific_objective_obj=so_obj)

class UpdateSpecificObjective(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        strategic_objective = String()
        specific_objective = String()
        actions_for_achievement = String()
        responsible_person = String()
        necessary_resources = String()
        indicator = String()
        goal = String()
        monitoring_frequency = String()
        deadline = Date()
        observation = String()
    
    specific_objective_obj = Field(SpecificObjectiveNode)
    
    def mutate(self, info, id, **kwargs):
        try:
            so_obj = SpecificObjective.objects.get(pk=id)
        except SpecificObjective.DoesNotExist:
            raise Exception("SpecificObjective not found")
        for key, value in kwargs.items():
            setattr(so_obj, key, value)
        so_obj.save()
        return UpdateSpecificObjective(specific_objective_obj=so_obj)

class DeleteSpecificObjective(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            so_obj = SpecificObjective.objects.get(pk=id)
        except SpecificObjective.DoesNotExist:
            raise Exception("SpecificObjective not found")
        so_obj.delete()
        return DeleteSpecificObjective(ok=True)

# -------------------------
# Root Mutation and Schema
# -------------------------

class Mutation(graphene.ObjectType):
    create_strategic_objective = CreateStrategicObjective.Field()
    update_strategic_objective = UpdateStrategicObjective.Field()
    delete_strategic_objective = DeleteStrategicObjective.Field()

    create_specific_objective = CreateSpecificObjective.Field()
    update_specific_objective = UpdateSpecificObjective.Field()
    delete_specific_objective = DeleteSpecificObjective.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
