import graphene
from graphene import Date, Int, String, List, Field
from graphene_django import DjangoObjectType

# Import models and Choices from your app
from .models import (
    TrainingNeeds,
    TrainingPlan,
    TrainingEvaluationQuestions,
    TrainingEffectivnessAssessment,
    Position,
    Training,
    ToolBoxTalks,
    TrainingMatrix,
    AcceptanceConfirmation,
    OHSACTING,
    # Choices enumerations (defined as models.Choices)
    TrainingTtype,
    Months,
    TrainingStatus,
    AnswerChoices,
    HumanResourceAnswerChoices,
    Effectiveness,
)
# Import related models for foreign keys
from riskmanagement.models import Department

# --------------------------------------------------------------------
# Create Graphene Enums from the Django Choices
# --------------------------------------------------------------------
TrainingTtypeEnum = graphene.Enum.from_enum(TrainingTtype)
MonthsEnum = graphene.Enum.from_enum(Months)
TrainingStatusEnum = graphene.Enum.from_enum(TrainingStatus)
AnswerChoicesEnum = graphene.Enum.from_enum(AnswerChoices)
HumanResourceAnswerChoicesEnum = graphene.Enum.from_enum(HumanResourceAnswerChoices)
EffectivenessEnum = graphene.Enum.from_enum(Effectiveness)

# --------------------------------------------------------------------
# Graphene Object Types for Models
# --------------------------------------------------------------------
class TrainingNeedsNode(DjangoObjectType):
    class Meta:
        model = TrainingNeeds
        fields = '__all__'

class TrainingPlanNode(DjangoObjectType):
    class Meta:
        model = TrainingPlan
        fields = '__all__'

class TrainingEvaluationQuestionsNode(DjangoObjectType):
    class Meta:
        model = TrainingEvaluationQuestions
        fields = '__all__'

class TrainingEffectivnessAssessmentNode(DjangoObjectType):
    class Meta:
        model = TrainingEffectivnessAssessment
        fields = '__all__'

class PositionNode(DjangoObjectType):
    class Meta:
        model = Position
        fields = '__all__'

class TrainingNode(DjangoObjectType):
    class Meta:
        model = Training
        fields = '__all__'

class ToolBoxTalksNode(DjangoObjectType):
    class Meta:
        model = ToolBoxTalks
        fields = '__all__'

class TrainingMatrixNode(DjangoObjectType):
    class Meta:
        model = TrainingMatrix
        fields = '__all__'

class AcceptanceConfirmationNode(DjangoObjectType):
    class Meta:
        model = AcceptanceConfirmation
        fields = '__all__'

class OHSACTINGNode(DjangoObjectType):
    class Meta:
        model = OHSACTING
        fields = '__all__'

# --------------------------------------------------------------------
# Queries
# --------------------------------------------------------------------
class Query(graphene.ObjectType):
    all_training_needs = List(TrainingNeedsNode)
    training_need = Field(TrainingNeedsNode, id=Int(required=True))

    all_training_plans = List(TrainingPlanNode)
    training_plan = Field(TrainingPlanNode, id=Int(required=True))

    all_training_evaluation_questions = List(TrainingEvaluationQuestionsNode)
    training_evaluation_question = Field(TrainingEvaluationQuestionsNode, id=Int(required=True))

    all_training_effectiveness_assessments = List(TrainingEffectivnessAssessmentNode)
    training_effectiveness_assessment = Field(TrainingEffectivnessAssessmentNode, id=Int(required=True))

    all_positions = List(PositionNode)
    position = Field(PositionNode, id=Int(required=True))

    all_trainings = List(TrainingNode)
    training = Field(TrainingNode, id=Int(required=True))

    all_toolbox_talks = List(ToolBoxTalksNode)
    toolbox_talk = Field(ToolBoxTalksNode, id=Int(required=True))

    all_training_matrices = List(TrainingMatrixNode)
    training_matrix = Field(TrainingMatrixNode, id=Int(required=True))

    all_acceptance_confirmations = List(AcceptanceConfirmationNode)
    acceptance_confirmation = Field(AcceptanceConfirmationNode, id=Int(required=True))

    all_ohs_actings = List(OHSACTINGNode)
    ohs_acting = Field(OHSACTINGNode, id=Int(required=True))

    def resolve_all_training_needs(root, info):
        return TrainingNeeds.objects.all()

    def resolve_training_need(root, info, id):
        try:
            return TrainingNeeds.objects.get(pk=id)
        except TrainingNeeds.DoesNotExist:
            return None

    def resolve_all_training_plans(root, info):
        return TrainingPlan.objects.all()

    def resolve_training_plan(root, info, id):
        try:
            return TrainingPlan.objects.get(pk=id)
        except TrainingPlan.DoesNotExist:
            return None

    def resolve_all_training_evaluation_questions(root, info):
        return TrainingEvaluationQuestions.objects.all()

    def resolve_training_evaluation_question(root, info, id):
        try:
            return TrainingEvaluationQuestions.objects.get(pk=id)
        except TrainingEvaluationQuestions.DoesNotExist:
            return None

    def resolve_all_training_effectiveness_assessments(root, info):
        return TrainingEffectivnessAssessment.objects.all()

    def resolve_training_effectiveness_assessment(root, info, id):
        try:
            return TrainingEffectivnessAssessment.objects.get(pk=id)
        except TrainingEffectivnessAssessment.DoesNotExist:
            return None

    def resolve_all_positions(root, info):
        return Position.objects.all()

    def resolve_position(root, info, id):
        try:
            return Position.objects.get(pk=id)
        except Position.DoesNotExist:
            return None

    def resolve_all_trainings(root, info):
        return Training.objects.all()

    def resolve_training(root, info, id):
        try:
            return Training.objects.get(pk=id)
        except Training.DoesNotExist:
            return None

    def resolve_all_toolbox_talks(root, info):
        return ToolBoxTalks.objects.all()

    def resolve_toolbox_talk(root, info, id):
        try:
            return ToolBoxTalks.objects.get(pk=id)
        except ToolBoxTalks.DoesNotExist:
            return None

    def resolve_all_training_matrices(root, info):
        return TrainingMatrix.objects.all()

    def resolve_training_matrix(root, info, id):
        try:
            return TrainingMatrix.objects.get(pk=id)
        except TrainingMatrix.DoesNotExist:
            return None

    def resolve_all_acceptance_confirmations(root, info):
        return AcceptanceConfirmation.objects.all()

    def resolve_acceptance_confirmation(root, info, id):
        try:
            return AcceptanceConfirmation.objects.get(pk=id)
        except AcceptanceConfirmation.DoesNotExist:
            return None

    def resolve_all_ohs_actings(root, info):
        return OHSACTING.objects.all()

    def resolve_ohs_acting(root, info, id):
        try:
            return OHSACTING.objects.get(pk=id)
        except OHSACTING.DoesNotExist:
            return None

# --------------------------------------------------------------------
# Mutations
# --------------------------------------------------------------------
# -- TrainingNeeds Mutations --
class CreateTrainingNeed(graphene.Mutation):
    class Arguments:
        filled_by = String(required=True)
        date = Date(required=True)
        department_id = Int(required=True)
        training = String(required=True)
        training_objective = String(required=True)
        proposal_of_training_entity = String(required=True)
        potential_training_participants = String(required=True)

    training_need = Field(TrainingNeedsNode)

    def mutate(self, info, filled_by, date, department_id, training, training_objective, proposal_of_training_entity, potential_training_participants):
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            raise Exception("Department not found")
        need = TrainingNeeds.objects.create(
            filled_by=filled_by,
            date=date,
            department=department,
            training=training,
            training_objective=training_objective,
            proposal_of_training_entity=proposal_of_training_entity,
            potential_training_participants=potential_training_participants
        )
        return CreateTrainingNeed(training_need=need)

class UpdateTrainingNeed(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        filled_by = String()
        date = Date()
        department_id = Int()
        training = String()
        training_objective = String()
        proposal_of_training_entity = String()
        potential_training_participants = String()

    training_need = Field(TrainingNeedsNode)

    def mutate(self, info, id, **kwargs):
        try:
            need = TrainingNeeds.objects.get(pk=id)
        except TrainingNeeds.DoesNotExist:
            raise Exception("TrainingNeed not found")
        if 'department_id' in kwargs:
            try:
                department = Department.objects.get(pk=kwargs.pop('department_id'))
                need.department = department
            except Department.DoesNotExist:
                raise Exception("Department not found")
        for key, value in kwargs.items():
            setattr(need, key, value)
        need.save()
        return UpdateTrainingNeed(training_need=need)

class DeleteTrainingNeed(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            need = TrainingNeeds.objects.get(pk=id)
        except TrainingNeeds.DoesNotExist:
            raise Exception("TrainingNeed not found")
        need.delete()
        return DeleteTrainingNeed(ok=True)

# -- TrainingPlan Mutations --
class CreateTrainingPlan(graphene.Mutation):
    class Arguments:
        updated_by = String(required=True)
        date = Date(required=True)
        year = Int(required=True)
        training_area = String(required=True)
        training_title = String(required=True)
        training_objective = String(required=True)
        training_type = TrainingTtypeEnum(required=True)
        training_entity = String(required=True)
        duration = String(required=True)
        number_of_trainees = Int(required=True)
        training_recipients = String(required=True)
        training_month = MonthsEnum(required=True)
        training_status = TrainingStatusEnum(required=True)
        observations = String(required=True)

    training_plan = Field(TrainingPlanNode)

    def mutate(self, info, updated_by, date, year, training_area, training_title,
               training_objective, training_type, training_entity, duration, number_of_trainees,
               training_recipients, training_month, training_status, observations):
        plan = TrainingPlan.objects.create(
            updated_by=updated_by,
            date=date,
            year=year,
            training_area=training_area,
            training_title=training_title,
            training_objective=training_objective,
            training_type=training_type,
            training_entity=training_entity,
            duration=duration,
            number_of_trainees=number_of_trainees,
            training_recipients=training_recipients,
            training_month=training_month,
            training_status=training_status,
            observations=observations
        )
        return CreateTrainingPlan(training_plan=plan)

class UpdateTrainingPlan(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        updated_by = String()
        date = Date()
        year = Int()
        training_area = String()
        training_title = String()
        training_objective = String()
        training_type = TrainingTtypeEnum()
        training_entity = String()
        duration = String()
        number_of_trainees = Int()
        training_recipients = String()
        training_month = MonthsEnum()
        training_status = TrainingStatusEnum()
        observations = String()

    training_plan = Field(TrainingPlanNode)

    def mutate(self, info, id, **kwargs):
        try:
            plan = TrainingPlan.objects.get(pk=id)
        except TrainingPlan.DoesNotExist:
            raise Exception("TrainingPlan not found")
        for key, value in kwargs.items():
            setattr(plan, key, value)
        plan.save()
        return UpdateTrainingPlan(training_plan=plan)

class DeleteTrainingPlan(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            plan = TrainingPlan.objects.get(pk=id)
        except TrainingPlan.DoesNotExist:
            raise Exception("TrainingPlan not found")
        plan.delete()
        return DeleteTrainingPlan(ok=True)

# -- TrainingEvaluationQuestions Mutations --
class CreateTrainingEvaluationQuestion(graphene.Mutation):
    class Arguments:
        question = String(required=True)
    training_evaluation_question = Field(TrainingEvaluationQuestionsNode)

    def mutate(self, info, question):
        qe = TrainingEvaluationQuestions.objects.create(question=question)
        return CreateTrainingEvaluationQuestion(training_evaluation_question=qe)

class UpdateTrainingEvaluationQuestion(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        question = String()
    training_evaluation_question = Field(TrainingEvaluationQuestionsNode)

    def mutate(self, info, id, question=None):
        try:
            qe = TrainingEvaluationQuestions.objects.get(pk=id)
        except TrainingEvaluationQuestions.DoesNotExist:
            raise Exception("TrainingEvaluationQuestion not found")
        if question is not None:
            qe.question = question
        qe.save()
        return UpdateTrainingEvaluationQuestion(training_evaluation_question=qe)

class DeleteTrainingEvaluationQuestion(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            qe = TrainingEvaluationQuestions.objects.get(pk=id)
        except TrainingEvaluationQuestions.DoesNotExist:
            raise Exception("TrainingEvaluationQuestion not found")
        qe.delete()
        return DeleteTrainingEvaluationQuestion(ok=True)

# -- TrainingEffectivnessAssessment Mutations --
class CreateTrainingEffectivenessAssessment(graphene.Mutation):
    class Arguments:
        training = String(required=True)
        date = Date(required=True)
        department_id = Int(required=True)
        trainee = String(required=True)
        immediate_supervisor = String(required=True)
        training_evaluation_question_id = Int(required=True)
        answer = AnswerChoicesEnum(required=True)
        human_resource_evaluation = HumanResourceAnswerChoicesEnum(required=True)

    training_effectiveness_assessment = Field(TrainingEffectivnessAssessmentNode)

    def mutate(self, info, training, date, department_id, trainee, immediate_supervisor,
               training_evaluation_question_id, answer, human_resource_evaluation):
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            raise Exception("Department not found")
        try:
            teq = TrainingEvaluationQuestions.objects.get(pk=training_evaluation_question_id)
        except TrainingEvaluationQuestions.DoesNotExist:
            raise Exception("TrainingEvaluationQuestion not found")
        assessment = TrainingEffectivnessAssessment.objects.create(
            training=training,
            date=date,
            department=department,
            trainee=trainee,
            immediate_supervisor=immediate_supervisor,
            training_evaluation_question=teq,
            answer=answer,
            human_resource_evaluation=human_resource_evaluation
        )
        return CreateTrainingEffectivenessAssessment(training_effectiveness_assessment=assessment)

class UpdateTrainingEffectivenessAssessment(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        training = String()
        date = Date()
        department_id = Int()
        trainee = String()
        immediate_supervisor = String()
        training_evaluation_question_id = Int()
        answer = AnswerChoicesEnum()
        human_resource_evaluation = HumanResourceAnswerChoicesEnum()

    training_effectiveness_assessment = Field(TrainingEffectivnessAssessmentNode)

    def mutate(self, info, id, **kwargs):
        try:
            assessment = TrainingEffectivnessAssessment.objects.get(pk=id)
        except TrainingEffectivnessAssessment.DoesNotExist:
            raise Exception("TrainingEffectivenessAssessment not found")
        if 'department_id' in kwargs:
            try:
                department = Department.objects.get(pk=kwargs.pop('department_id'))
                assessment.department = department
            except Department.DoesNotExist:
                raise Exception("Department not found")
        if 'training_evaluation_question_id' in kwargs:
            try:
                teq = TrainingEvaluationQuestions.objects.get(pk=kwargs.pop('training_evaluation_question_id'))
                assessment.training_evaluation_question = teq
            except TrainingEvaluationQuestions.DoesNotExist:
                raise Exception("TrainingEvaluationQuestion not found")
        for key, value in kwargs.items():
            setattr(assessment, key, value)
        assessment.save()
        return UpdateTrainingEffectivenessAssessment(training_effectiveness_assessment=assessment)

class DeleteTrainingEffectivenessAssessment(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            assessment = TrainingEffectivnessAssessment.objects.get(pk=id)
        except TrainingEffectivnessAssessment.DoesNotExist:
            raise Exception("TrainingEffectivenessAssessment not found")
        assessment.delete()
        return DeleteTrainingEffectivenessAssessment(ok=True)

# -- Position Mutations --
class CreatePosition(graphene.Mutation):
    class Arguments:
        name = String(required=True)
    position = Field(PositionNode)

    def mutate(self, info, name):
        pos = Position.objects.create(name=name)
        return CreatePosition(position=pos)

class UpdatePosition(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
    position = Field(PositionNode)

    def mutate(self, info, id, name=None):
        try:
            pos = Position.objects.get(pk=id)
        except Position.DoesNotExist:
            raise Exception("Position not found")
        if name is not None:
            pos.name = name
        pos.save()
        return UpdatePosition(position=pos)

class DeletePosition(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            pos = Position.objects.get(pk=id)
        except Position.DoesNotExist:
            raise Exception("Position not found")
        pos.delete()
        return DeletePosition(ok=True)

# -- Training Mutations --
class CreateTraining(graphene.Mutation):
    class Arguments:
        name = String(required=True)
    training = Field(TrainingNode)

    def mutate(self, info, name):
        train = Training.objects.create(name=name)
        return CreateTraining(training=train)

class UpdateTraining(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
    training = Field(TrainingNode)

    def mutate(self, info, id, name=None):
        try:
            train = Training.objects.get(pk=id)
        except Training.DoesNotExist:
            raise Exception("Training not found")
        if name is not None:
            train.name = name
        train.save()
        return UpdateTraining(training=train)

class DeleteTraining(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            train = Training.objects.get(pk=id)
        except Training.DoesNotExist:
            raise Exception("Training not found")
        train.delete()
        return DeleteTraining(ok=True)

# -- ToolBoxTalks Mutations --
class CreateToolBoxTalks(graphene.Mutation):
    class Arguments:
        name = String(required=True)
    toolbox_talks = Field(ToolBoxTalksNode)

    def mutate(self, info, name):
        tbt = ToolBoxTalks.objects.create(name=name)
        return CreateToolBoxTalks(toolbox_talks=tbt)

class UpdateToolBoxTalks(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
    toolbox_talks = Field(ToolBoxTalksNode)

    def mutate(self, info, id, name=None):
        try:
            tbt = ToolBoxTalks.objects.get(pk=id)
        except ToolBoxTalks.DoesNotExist:
            raise Exception("ToolBoxTalks not found")
        if name is not None:
            tbt.name = name
        tbt.save()
        return UpdateToolBoxTalks(toolbox_talks=tbt)

class DeleteToolBoxTalks(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            tbt = ToolBoxTalks.objects.get(pk=id)
        except ToolBoxTalks.DoesNotExist:
            raise Exception("ToolBoxTalks not found")
        tbt.delete()
        return DeleteToolBoxTalks(ok=True)

# -- TrainingMatrix Mutations --
class CreateTrainingMatrix(graphene.Mutation):
    class Arguments:
        date = Date()
        position_id = Int(required=True)
        training_id = Int(required=True)
        toolbox_talks_id = Int(required=True)
        effectiveness = EffectivenessEnum(required=True)
        actions_training_not_effective = String()
        approved_by = String(required=True)

    training_matrix = Field(TrainingMatrixNode)

    def mutate(self, info, position_id, training_id, toolbox_talks_id, effectiveness, approved_by, date=None, actions_training_not_effective=None):
        try:
            pos = Position.objects.get(pk=position_id)
        except Position.DoesNotExist:
            raise Exception("Position not found")
        try:
            train = Training.objects.get(pk=training_id)
        except Training.DoesNotExist:
            raise Exception("Training not found")
        try:
            tbt = ToolBoxTalks.objects.get(pk=toolbox_talks_id)
        except ToolBoxTalks.DoesNotExist:
            raise Exception("ToolBoxTalks not found")
        matrix = TrainingMatrix.objects.create(
            date=date,
            position=pos,
            training=train,
            toolbox_talks=tbt,
            effectiveness=effectiveness,
            actions_training_not_effective=actions_training_not_effective,
            approved_by=approved_by
        )
        return CreateTrainingMatrix(training_matrix=matrix)

class UpdateTrainingMatrix(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        date = Date()
        position_id = Int()
        training_id = Int()
        toolbox_talks_id = Int()
        effectiveness = EffectivenessEnum()
        actions_training_not_effective = String()
        approved_by = String()

    training_matrix = Field(TrainingMatrixNode)

    def mutate(self, info, id, **kwargs):
        try:
            matrix = TrainingMatrix.objects.get(pk=id)
        except TrainingMatrix.DoesNotExist:
            raise Exception("TrainingMatrix not found")
        if 'position_id' in kwargs:
            try:
                pos = Position.objects.get(pk=kwargs.pop('position_id'))
                matrix.position = pos
            except Position.DoesNotExist:
                raise Exception("Position not found")
        if 'training_id' in kwargs:
            try:
                train = Training.objects.get(pk=kwargs.pop('training_id'))
                matrix.training = train
            except Training.DoesNotExist:
                raise Exception("Training not found")
        if 'toolbox_talks_id' in kwargs:
            try:
                tbt = ToolBoxTalks.objects.get(pk=kwargs.pop('toolbox_talks_id'))
                matrix.toolbox_talks = tbt
            except ToolBoxTalks.DoesNotExist:
                raise Exception("ToolBoxTalks not found")
        for key, value in kwargs.items():
            setattr(matrix, key, value)
        matrix.save()
        return UpdateTrainingMatrix(training_matrix=matrix)

class DeleteTrainingMatrix(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            matrix = TrainingMatrix.objects.get(pk=id)
        except TrainingMatrix.DoesNotExist:
            raise Exception("TrainingMatrix not found")
        matrix.delete()
        return DeleteTrainingMatrix(ok=True)

# -- AcceptanceConfirmation Mutations --
class CreateAcceptanceConfirmation(graphene.Mutation):
    class Arguments:
        description = String(required=True)
    acceptance_confirmation = Field(AcceptanceConfirmationNode)

    def mutate(self, info, description):
        ac = AcceptanceConfirmation.objects.create(description=description)
        return CreateAcceptanceConfirmation(acceptance_confirmation=ac)

class UpdateAcceptanceConfirmation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        description = String()
    acceptance_confirmation = Field(AcceptanceConfirmationNode)

    def mutate(self, info, id, description=None):
        try:
            ac = AcceptanceConfirmation.objects.get(pk=id)
        except AcceptanceConfirmation.DoesNotExist:
            raise Exception("AcceptanceConfirmation not found")
        if description is not None:
            ac.description = description
        ac.save()
        return UpdateAcceptanceConfirmation(acceptance_confirmation=ac)

class DeleteAcceptanceConfirmation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            ac = AcceptanceConfirmation.objects.get(pk=id)
        except AcceptanceConfirmation.DoesNotExist:
            raise Exception("AcceptanceConfirmation not found")
        ac.delete()
        return DeleteAcceptanceConfirmation(ok=True)

# -- OHSACTING Mutations --
class CreateOHSACTING(graphene.Mutation):
    class Arguments:
        fullname = String(required=True)
        designation = String()
        terms_of_office_from = String()
        terms_of_office_to = String()
        # For many-to-many field, pass a list of AcceptanceConfirmation IDs.
        acceptance_confirmation_ids = List(Int)
    ohs_acting = Field(OHSACTINGNode)

    def mutate(self, info, fullname, designation=None, terms_of_office_from=None, terms_of_office_to=None, acceptance_confirmation_ids=None):
        ohs = OHSACTING.objects.create(
            fullname=fullname,
            designation=designation,
            terms_of_office_from=terms_of_office_from,
            terms_of_office_to=terms_of_office_to,
        )
        if acceptance_confirmation_ids:
            ac_objects = AcceptanceConfirmation.objects.filter(pk__in=acceptance_confirmation_ids)
            ohs.acceptance_confirmation.set(ac_objects)
        return CreateOHSACTING(ohs_acting=ohs)

class UpdateOHSACTING(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        fullname = String()
        designation = String()
        terms_of_office_from = String()
        terms_of_office_to = String()
        acceptance_confirmation_ids = List(Int)
    ohs_acting = Field(OHSACTINGNode)

    def mutate(self, info, id, **kwargs):
        try:
            ohs = OHSACTING.objects.get(pk=id)
        except OHSACTING.DoesNotExist:
            raise Exception("OHSACTING not found")
        if 'acceptance_confirmation_ids' in kwargs:
            ids = kwargs.pop('acceptance_confirmation_ids')
            if ids:
                ac_objects = AcceptanceConfirmation.objects.filter(pk__in=ids)
                ohs.acceptance_confirmation.set(ac_objects)
        for key, value in kwargs.items():
            setattr(ohs, key, value)
        ohs.save()
        return UpdateOHSACTING(ohs_acting=ohs)

class DeleteOHSACTING(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            ohs = OHSACTING.objects.get(pk=id)
        except OHSACTING.DoesNotExist:
            raise Exception("OHSACTING not found")
        ohs.delete()
        return DeleteOHSACTING(ok=True)

# --------------------------------------------------------------------
# Root Mutation and Schema
# --------------------------------------------------------------------
class Mutation(graphene.ObjectType):
    create_training_need = CreateTrainingNeed.Field()
    update_training_need = UpdateTrainingNeed.Field()
    delete_training_need = DeleteTrainingNeed.Field()

    create_training_plan = CreateTrainingPlan.Field()
    update_training_plan = UpdateTrainingPlan.Field()
    delete_training_plan = DeleteTrainingPlan.Field()

    create_training_evaluation_question = CreateTrainingEvaluationQuestion.Field()
    update_training_evaluation_question = UpdateTrainingEvaluationQuestion.Field()
    delete_training_evaluation_question = DeleteTrainingEvaluationQuestion.Field()

    create_training_effectiveness_assessment = CreateTrainingEffectivenessAssessment.Field()
    update_training_effectiveness_assessment = UpdateTrainingEffectivenessAssessment.Field()
    delete_training_effectiveness_assessment = DeleteTrainingEffectivenessAssessment.Field()

    create_position = CreatePosition.Field()
    update_position = UpdatePosition.Field()
    delete_position = DeletePosition.Field()

    create_training = CreateTraining.Field()
    update_training = UpdateTraining.Field()
    delete_training = DeleteTraining.Field()

    create_toolbox_talks = CreateToolBoxTalks.Field()
    update_toolbox_talks = UpdateToolBoxTalks.Field()
    delete_toolbox_talks = DeleteToolBoxTalks.Field()

    create_training_matrix = CreateTrainingMatrix.Field()
    update_training_matrix = UpdateTrainingMatrix.Field()
    delete_training_matrix = DeleteTrainingMatrix.Field()

    create_acceptance_confirmation = CreateAcceptanceConfirmation.Field()
    update_acceptance_confirmation = UpdateAcceptanceConfirmation.Field()
    delete_acceptance_confirmation = DeleteAcceptanceConfirmation.Field()

    create_ohs_acting = CreateOHSACTING.Field()
    update_ohs_acting = UpdateOHSACTING.Field()
    delete_ohs_acting = DeleteOHSACTING.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
