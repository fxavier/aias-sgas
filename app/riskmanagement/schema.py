import graphene
from graphene import Date, DateTime, Int, String, Decimal, List, Field
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

# Import models and Django choices
from .models import (
    Department,
    EnvironmentalFactor,
    EnvironAndSocialRiskAndImapactAssessement,
    LegalRequirementControl,
    ContactPerson,
    ResponsibleForFillingForm,
    ResponsibleForVerification,
    BiodeversidadeRecursosNaturais,
    Subproject,
    EnvironmentalSocialScreening,
    ConsultationAndEngagement,
    ScreeningResult,
    PreliminaryEnvironmentalInformation,
    EmbeddedMitigation,
    PlanningOrConstructionPhase,
    # For Preliminary Environmental Information choices:
    Provinces,
    ActivityType,
    DevelopmentStage,
    InsertionPoint,
    TerritorialPlanningFramework,
    PyhsicalCharacteristics,
    PredominantEcosystems,
    LocationZone,
    TypeOfPredominantVegetation,
    LandUse,
    # For EnvironAndSocialRiskAndImapactAssessement choices:
    Duration,
    Extension,
    Intensity,
    LifeCycle,
    Probability,
    ResponseType,
    Statute,
    Status as ModelStatus,
)
from users.models import User

# --------------------------------------------------------------------
# Create Graphene Enums from Django TextChoices and Inline Choices
# --------------------------------------------------------------------
DurationEnum = graphene.Enum.from_enum(Duration)
ExtensionEnum = graphene.Enum.from_enum(Extension)
IntensityEnum = graphene.Enum.from_enum(Intensity)
LifeCycleEnum = graphene.Enum.from_enum(LifeCycle)
ProbabilityEnum = graphene.Enum.from_enum(Probability)
ResponseTypeEnum = graphene.Enum.from_enum(ResponseType)
StatuteEnum = graphene.Enum.from_enum(Statute)
RiskManagementStatusEnum = graphene.Enum(
    "RiskManagementStatus",
    {member.name: member.value for member in ModelStatus}
)


ActivityTypeEnum = graphene.Enum.from_enum(ActivityType)
DevelopmentStageEnum = graphene.Enum.from_enum(DevelopmentStage)
InsertionPointEnum = graphene.Enum.from_enum(InsertionPoint)
TerritorialPlanningFrameworkEnum = graphene.Enum.from_enum(TerritorialPlanningFramework)
PyhsicalCharacteristicsEnum = graphene.Enum.from_enum(PyhsicalCharacteristics)
PredominantEcosystemsEnum = graphene.Enum.from_enum(PredominantEcosystems)
LocationZoneEnum = graphene.Enum.from_enum(LocationZone)
TypeOfPredominantVegetationEnum = graphene.Enum.from_enum(TypeOfPredominantVegetation)
LandUseEnum = graphene.Enum.from_enum(LandUse)
ProvincesEnum = graphene.Enum.from_enum(Provinces)

# ScreeningResult risk category is inline
ScreeningRiskCategoryEnum = graphene.Enum(
    'ScreeningRiskCategoryEnum',
    [('ALTO', 'Alto Risco'),
     ('SUBSTANCIAL', 'Risco Substancial'),
     ('MODERADO', 'Risco Moderado'),
     ('BAIXO', 'Risco Baixo')]
)

# --------------------------------------------------------------------
# Graphene Object Types
# --------------------------------------------------------------------
class DepartmentNode(DjangoObjectType):
    class Meta:
        model = Department
        fields = '__all__'

class EnvironmentalFactorNode(DjangoObjectType):
    class Meta:
        model = EnvironmentalFactor
        fields = '__all__'

class EnvironAndSocialRiskAndImapactAssessementNode(DjangoObjectType):
    class Meta:
        model = EnvironAndSocialRiskAndImapactAssessement
        fields = '__all__'

class LegalRequirementControlNode(DjangoObjectType):
    class Meta:
        model = LegalRequirementControl
        fields = '__all__'

class ContactPersonNode(DjangoObjectType):
    class Meta:
        model = ContactPerson
        fields = '__all__'

class ResponsibleForFillingFormNode(DjangoObjectType):
    class Meta:
        model = ResponsibleForFillingForm
        fields = '__all__'

class ResponsibleForVerificationNode(DjangoObjectType):
    class Meta:
        model = ResponsibleForVerification
        fields = '__all__'

class BiodeversidadeRecursosNaturaisNode(DjangoObjectType):
    class Meta:
        model = BiodeversidadeRecursosNaturais
        fields = '__all__'

class SubprojectNode(DjangoObjectType):
    class Meta:
        model = Subproject
        fields = '__all__'

class EnvironmentalSocialScreeningNode(DjangoObjectType):
    class Meta:
        model = EnvironmentalSocialScreening
        fields = '__all__'

class ConsultationAndEngagementNode(DjangoObjectType):
    class Meta:
        model = ConsultationAndEngagement
        fields = '__all__'

class ScreeningResultNode(DjangoObjectType):
    class Meta:
        model = ScreeningResult
        fields = '__all__'

class PreliminaryEnvironmentalInformationNode(DjangoObjectType):
    class Meta:
        model = PreliminaryEnvironmentalInformation
        fields = '__all__'

class EmbeddedMitigationNode(DjangoObjectType):
    class Meta:
        model = EmbeddedMitigation
        fields = '__all__'

class PlanningOrConstructionPhaseNode(DjangoObjectType):
    class Meta:
        model = PlanningOrConstructionPhase
        fields = '__all__'

# --------------------------------------------------------------------
# Queries
# --------------------------------------------------------------------
class Query(graphene.ObjectType):
    # For brevity, we expose queries for most models
    all_departments = List(DepartmentNode)
    department = Field(DepartmentNode, id=Int(required=True))
    
    all_environmental_factors = List(EnvironmentalFactorNode)
    all_environ_social_assessments = List(EnvironAndSocialRiskAndImapactAssessementNode)
    environ_social_assessment = Field(EnvironAndSocialRiskAndImapactAssessementNode, id=Int(required=True))
    
    all_legal_requirement_controls = List(LegalRequirementControlNode)
    legal_requirement_control = Field(LegalRequirementControlNode, id=Int(required=True))
    
    all_contact_persons = List(ContactPersonNode)
    contact_person = Field(ContactPersonNode, id=Int(required=True))
    
    all_biodeversidade_recursos = List(BiodeversidadeRecursosNaturaisNode)
    biodeversidade_recursos = Field(BiodeversidadeRecursosNaturaisNode, id=Int(required=True))
    
    all_subprojects = List(SubprojectNode)
    subproject = Field(SubprojectNode, id=Int(required=True))
    
    all_environmental_social_screenings = List(EnvironmentalSocialScreeningNode)
    environmental_social_screening = Field(EnvironmentalSocialScreeningNode, id=Int(required=True))
    
    all_consultations = List(ConsultationAndEngagementNode)
    consultation = Field(ConsultationAndEngagementNode, id=Int(required=True))
    
    all_screening_results = List(ScreeningResultNode)
    screening_result = Field(ScreeningResultNode, id=Int(required=True))
    
    all_preliminary_env_infos = List(PreliminaryEnvironmentalInformationNode)
    preliminary_env_info = Field(PreliminaryEnvironmentalInformationNode, id=Int(required=True))
    
    all_embedded_mitigations = List(EmbeddedMitigationNode)
    embedded_mitigation = Field(EmbeddedMitigationNode, id=Int(required=True))
    
    all_planning_construction_phases = List(PlanningOrConstructionPhaseNode)
    planning_construction_phase = Field(PlanningOrConstructionPhaseNode, id=Int(required=True))
    
    def resolve_all_departments(root, info):
        return Department.objects.all()
    
    def resolve_department(root, info, id):
        try:
            return Department.objects.get(pk=id)
        except Department.DoesNotExist:
            return None
    
    def resolve_all_environmental_factors(root, info):
        return EnvironmentalFactor.objects.all()
    
    def resolve_all_environ_social_assessments(root, info):
        return EnvironAndSocialRiskAndImapactAssessement.objects.all()
    
    def resolve_environ_social_assessment(root, info, id):
        try:
            return EnvironAndSocialRiskAndImapactAssessement.objects.get(pk=id)
        except EnvironAndSocialRiskAndImapactAssessement.DoesNotExist:
            return None
    
    def resolve_all_legal_requirement_controls(root, info):
        return LegalRequirementControl.objects.all()
    
    def resolve_legal_requirement_control(root, info, id):
        try:
            return LegalRequirementControl.objects.get(pk=id)
        except LegalRequirementControl.DoesNotExist:
            return None
    
    def resolve_all_contact_persons(root, info):
        return ContactPerson.objects.all()
    
    def resolve_contact_person(root, info, id):
        try:
            return ContactPerson.objects.get(pk=id)
        except ContactPerson.DoesNotExist:
            return None
    
    def resolve_all_biodeversidade_recursos(root, info):
        return BiodeversidadeRecursosNaturais.objects.all()
    
    def resolve_biodeversidade_recursos(root, info, id):
        try:
            return BiodeversidadeRecursosNaturais.objects.get(pk=id)
        except BiodeversidadeRecursosNaturais.DoesNotExist:
            return None
    
    def resolve_all_subprojects(root, info):
        return Subproject.objects.all()
    
    def resolve_subproject(root, info, id):
        try:
            return Subproject.objects.get(pk=id)
        except Subproject.DoesNotExist:
            return None
    
    def resolve_all_environmental_social_screenings(root, info):
        return EnvironmentalSocialScreening.objects.all()
    
    def resolve_environmental_social_screening(root, info, id):
        try:
            return EnvironmentalSocialScreening.objects.get(pk=id)
        except EnvironmentalSocialScreening.DoesNotExist:
            return None
    
    def resolve_all_consultations(root, info):
        return ConsultationAndEngagement.objects.all()
    
    def resolve_consultation(root, info, id):
        try:
            return ConsultationAndEngagement.objects.get(pk=id)
        except ConsultationAndEngagement.DoesNotExist:
            return None
    
    def resolve_all_screening_results(root, info):
        return ScreeningResult.objects.all()
    
    def resolve_screening_result(root, info, id):
        try:
            return ScreeningResult.objects.get(pk=id)
        except ScreeningResult.DoesNotExist:
            return None
    
    def resolve_all_preliminary_env_infos(root, info):
        return PreliminaryEnvironmentalInformation.objects.all()
    
    def resolve_preliminary_env_info(root, info, id):
        try:
            return PreliminaryEnvironmentalInformation.objects.get(pk=id)
        except PreliminaryEnvironmentalInformation.DoesNotExist:
            return None
    
    def resolve_all_embedded_mitigations(root, info):
        return EmbeddedMitigation.objects.all()
    
    def resolve_embedded_mitigation(root, info, id):
        try:
            return EmbeddedMitigation.objects.get(pk=id)
        except EmbeddedMitigation.DoesNotExist:
            return None
    
    def resolve_all_planning_construction_phases(root, info):
        return PlanningOrConstructionPhase.objects.all()
    
    def resolve_planning_construction_phase(root, info, id):
        try:
            return PlanningOrConstructionPhase.objects.get(pk=id)
        except PlanningOrConstructionPhase.DoesNotExist:
            return None

# --------------------------------------------------------------------
# Mutations
# --------------------------------------------------------------------
# For brevity, each model gets Create/Update/Delete mutations following a similar pattern.
# You can expand error handling as needed.

# --- EnvironAndSocialRiskAndImapactAssessement Mutations ---
class CreateEnvironAndSocialRiskAndImapactAssessement(graphene.Mutation):
    class Arguments:
        departament_id = Int(required=True)
        activity = String(required=True)
        risks_and_impact_id = Int(required=True)
        environmental_factor_id = Int(required=True)
        life_cycle = LifeCycleEnum(required=True)
        statute = StatuteEnum(required=True)
        extension = ExtensionEnum(required=True)
        duration = DurationEnum(required=True)
        intensity = IntensityEnum(required=True)
        probability = ProbabilityEnum(required=True)
        description_of_measures = String(required=True)
        deadline = String(required=True)
        responsible_id = Int()  # optional
        effectiveness_assessment = String(required=True)
        legal_requirements_ids = List(Int)  # many-to-many
        compliance_requirements = String(required=True)
        observations = String(required=True)
        created_by_id = Int(required=True)
    environ_social_assessment = Field(EnvironAndSocialRiskAndImapactAssessementNode)
    def mutate(self, info, departament_id, activity, risks_and_impact_id,
               environmental_factor_id, life_cycle, statute, extension, duration,
               intensity, probability, description_of_measures, deadline, effectiveness_assessment,
               compliance_requirements, observations, created_by_id, responsible_id=None, legal_requirements_ids=None):
        # Fetch foreign key objects
        try:
            dept = Department.objects.get(pk=departament_id)
        except Department.DoesNotExist:
            raise Exception("Department not found")
        # risks_and_impact and environmental_factor would normally be looked up similarly;
        # here we assume their IDs are passed (adjust as needed)
        from .models import RisksAndImpact  # import if needed
        try:
            risks = RisksAndImpact.objects.get(pk=risks_and_impact_id)
        except RisksAndImpact.DoesNotExist:
            raise Exception("RisksAndImpact not found")
        try:
            env_factor = EnvironmentalFactor.objects.get(pk=environmental_factor_id)
        except EnvironmentalFactor.DoesNotExist:
            raise Exception("EnvironmentalFactor not found")
        responsible = None
        if responsible_id:
            try:
                responsible = User.objects.get(pk=responsible_id)
            except User.DoesNotExist:
                raise Exception("Responsible user not found")
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("Created_by user not found")
        assessment = EnvironAndSocialRiskAndImapactAssessement.objects.create(
            departament=dept,
            activity=activity,
            risks_and_impact=risks,
            environmental_factor=env_factor,
            life_cycle=life_cycle,
            statute=statute,
            extension=extension,
            duration=duration,
            intensity=intensity,
            probability=probability,
            description_of_measures=description_of_measures,
            deadline=deadline,
            responsible=responsible,
            effectiveness_assessment=effectiveness_assessment,
            compliance_requirements=compliance_requirements,
            observations=observations,
            created_by=created_by
        )
        if legal_requirements_ids:
            assessment.legal_requirements.set(legal_requirements_ids)
        return CreateEnvironAndSocialRiskAndImapactAssessement(environ_social_assessment=assessment)

class UpdateEnvironAndSocialRiskAndImapactAssessement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        activity = String()
        life_cycle = LifeCycleEnum()
        statute = StatuteEnum()
        extension = ExtensionEnum()
        duration = DurationEnum()
        intensity = IntensityEnum()
        probability = ProbabilityEnum()
        description_of_measures = String()
        deadline = String()
        effectiveness_assessment = String()
        compliance_requirements = String()
        observations = String()
        legal_requirements_ids = List(Int)
    environ_social_assessment = Field(EnvironAndSocialRiskAndImapactAssessementNode)
    def mutate(self, info, id, **kwargs):
        try:
            assessment = EnvironAndSocialRiskAndImapactAssessement.objects.get(pk=id)
        except EnvironAndSocialRiskAndImapactAssessement.DoesNotExist:
            raise Exception("Assessment not found")
        if 'legal_requirements_ids' in kwargs:
            ids = kwargs.pop('legal_requirements_ids')
            assessment.legal_requirements.set(ids)
        for key, value in kwargs.items():
            setattr(assessment, key, value)
        assessment.save()
        return UpdateEnvironAndSocialRiskAndImapactAssessement(environ_social_assessment=assessment)

class DeleteEnvironAndSocialRiskAndImapactAssessement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            assessment = EnvironAndSocialRiskAndImapactAssessement.objects.get(pk=id)
        except EnvironAndSocialRiskAndImapactAssessement.DoesNotExist:
            raise Exception("Assessment not found")
        assessment.delete()
        return DeleteEnvironAndSocialRiskAndImapactAssessement(ok=True)

# --- LegalRequirementControl Mutations ---
class CreateLegalRequirementControl(graphene.Mutation):
    class Arguments:
        number = String(required=True)
        document_title = String(required=True)
        effective_date = Date(required=True)
        description = String(required=True)
        status = RiskManagementStatusEnum(required=True)
        amended_description = String()
        observation = String()
        law_file = Upload()  # file upload
        created_by_id = Int(required=True)
    legal_requirement_control = Field(LegalRequirementControlNode)
    def mutate(self, info, number, document_title, effective_date, description,
               status, created_by_id, amended_description=None, observation=None, law_file=None):
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        control = LegalRequirementControl.objects.create(
            number=number,
            document_title=document_title,
            effective_date=effective_date,
            description=description,
            status=status,
            amended_description=amended_description,
            observation=observation,
            law_file=law_file,
            created_by=created_by
        )
        return CreateLegalRequirementControl(legal_requirement_control=control)

class UpdateLegalRequirementControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        number = String()
        document_title = String()
        effective_date = Date()
        description = String()
        status = RiskManagementStatusEnum()
        amended_description = String()
        observation = String()
        law_file = Upload()
    legal_requirement_control = Field(LegalRequirementControlNode)
    def mutate(self, info, id, **kwargs):
        try:
            control = LegalRequirementControl.objects.get(pk=id)
        except LegalRequirementControl.DoesNotExist:
            raise Exception("LegalRequirementControl not found")
        for key, value in kwargs.items():
            setattr(control, key, value)
        control.save()
        return UpdateLegalRequirementControl(legal_requirement_control=control)

class DeleteLegalRequirementControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            control = LegalRequirementControl.objects.get(pk=id)
        except LegalRequirementControl.DoesNotExist:
            raise Exception("LegalRequirementControl not found")
        control.delete()
        return DeleteLegalRequirementControl(ok=True)

# --- ContactPerson and Derived Mutations ---
class CreateContactPerson(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        role = String(required=True)
        contact = String(required=True)
        date = Date(required=True)
        signature = String()
    contact_person = Field(ContactPersonNode)
    def mutate(self, info, name, role, contact, date, signature=None):
        cp = ContactPerson.objects.create(
            name=name,
            role=role,
            contact=contact,
            date=date,
            signature=signature
        )
        return CreateContactPerson(contact_person=cp)

class UpdateContactPerson(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        role = String()
        contact = String()
        date = Date()
        signature = String()
    contact_person = Field(ContactPersonNode)
    def mutate(self, info, id, **kwargs):
        try:
            cp = ContactPerson.objects.get(pk=id)
        except ContactPerson.DoesNotExist:
            raise Exception("ContactPerson not found")
        for key, value in kwargs.items():
            setattr(cp, key, value)
        cp.save()
        return UpdateContactPerson(contact_person=cp)

class DeleteContactPerson(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            cp = ContactPerson.objects.get(pk=id)
        except ContactPerson.DoesNotExist:
            raise Exception("ContactPerson not found")
        cp.delete()
        return DeleteContactPerson(ok=True)

# (Mutations for ResponsibleForFillingForm and ResponsibleForVerification can reuse ContactPerson mutations.)

# --- BiodeversidadeRecursosNaturais Mutations ---
class CreateBiodeversidadeRecursosNaturais(graphene.Mutation):
    class Arguments:
        reference = String()
        description = String(required=True)
    biodeversidade = Field(BiodeversidadeRecursosNaturaisNode)
    def mutate(self, info, description, reference=None):
        bio = BiodeversidadeRecursosNaturais.objects.create(
            reference=reference,
            description=description
        )
        return CreateBiodeversidadeRecursosNaturais(biodeversidade=bio)

class UpdateBiodeversidadeRecursosNaturais(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        reference = String()
        description = String()
    biodeversidade = Field(BiodeversidadeRecursosNaturaisNode)
    def mutate(self, info, id, **kwargs):
        try:
            bio = BiodeversidadeRecursosNaturais.objects.get(pk=id)
        except BiodeversidadeRecursosNaturais.DoesNotExist:
            raise Exception("BiodeversidadeRecursosNaturais not found")
        for key, value in kwargs.items():
            setattr(bio, key, value)
        bio.save()
        return UpdateBiodeversidadeRecursosNaturais(biodeversidade=bio)

class DeleteBiodeversidadeRecursosNaturais(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            bio = BiodeversidadeRecursosNaturais.objects.get(pk=id)
        except BiodeversidadeRecursosNaturais.DoesNotExist:
            raise Exception("BiodeversidadeRecursosNaturais not found")
        bio.delete()
        return DeleteBiodeversidadeRecursosNaturais(ok=True)

# --- Subproject Mutations ---
class CreateSubproject(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        contract_reference = String()
        contractor_name = String()
        estimated_cost = Decimal()
        location = String(required=True)
        geographic_coordinates = String()
        type = String(required=True)
        approximate_area = String(required=True)
    subproject = Field(SubprojectNode)
    def mutate(self, info, name, location, type, approximate_area, contract_reference=None,
               contractor_name=None, estimated_cost=None, geographic_coordinates=None):
        sub = Subproject.objects.create(
            name=name,
            contract_reference=contract_reference,
            contractor_name=contractor_name,
            estimated_cost=estimated_cost,
            location=location,
            geographic_coordinates=geographic_coordinates,
            type=type,
            approximate_area=approximate_area
        )
        return CreateSubproject(subproject=sub)

class UpdateSubproject(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        contract_reference = String()
        contractor_name = String()
        estimated_cost = Decimal()
        location = String()
        geographic_coordinates = String()
        type = String()
        approximate_area = String()
    subproject = Field(SubprojectNode)
    def mutate(self, info, id, **kwargs):
        try:
            sub = Subproject.objects.get(pk=id)
        except Subproject.DoesNotExist:
            raise Exception("Subproject not found")
        for key, value in kwargs.items():
            setattr(sub, key, value)
        sub.save()
        return UpdateSubproject(subproject=sub)

class DeleteSubproject(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            sub = Subproject.objects.get(pk=id)
        except Subproject.DoesNotExist:
            raise Exception("Subproject not found")
        sub.delete()
        return DeleteSubproject(ok=True)

# --- EnvironmentalSocialScreening Mutations ---
class CreateEnvironmentalSocialScreening(graphene.Mutation):
    class Arguments:
        responsible_for_filling_form_id = Int(required=True)
        responsible_for_verification_id = Int(required=True)
        subproject_id = Int(required=True)
        biodiversidade_recursos_naturais_id = Int(required=True)
        response = String(required=True)
        comment = String()
        relevant_standard = String()
        consultation_and_engagement = String()
        recomended_actions = String()
        screening_results_id = Int(required=True)
        created_by_id = Int(required=True)
    environmental_social_screening = Field(EnvironmentalSocialScreeningNode)
    def mutate(self, info, responsible_for_filling_form_id, responsible_for_verification_id,
               subproject_id, biodiversidade_recursos_naturais_id, response, screening_results_id,
               created_by_id, comment=None, relevant_standard=None, consultation_and_engagement=None,
               recomended_actions=None):
        try:
            rff = ResponsibleForFillingForm.objects.get(pk=responsible_for_filling_form_id)
            rv = ResponsibleForVerification.objects.get(pk=responsible_for_verification_id)
            sub = Subproject.objects.get(pk=subproject_id)
            bio = BiodeversidadeRecursosNaturais.objects.get(pk=biodiversidade_recursos_naturais_id)
            screening = ScreeningResult.objects.get(pk=screening_results_id)
            created_by = User.objects.get(pk=created_by_id)
        except Exception as e:
            raise Exception(f"Foreign key error: {str(e)}")
        screening_form = EnvironmentalSocialScreening.objects.create(
            responsible_for_filling_form=rff,
            responsible_for_verification=rv,
            subproject=sub,
            biodiversidade_recursos_naturais=bio,
            response=response,
            screening_results=screening,
            created_by=created_by,
            comment=comment,
            relevant_standard=relevant_standard,
            consultation_and_engagement=consultation_and_engagement,
            recomended_actions=recomended_actions
        )
        return CreateEnvironmentalSocialScreening(environmental_social_screening=screening_form)

class UpdateEnvironmentalSocialScreening(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        response = String()
        comment = String()
        relevant_standard = String()
        consultation_and_engagement = String()
        recomended_actions = String()
    environmental_social_screening = Field(EnvironmentalSocialScreeningNode)
    def mutate(self, info, id, **kwargs):
        try:
            form = EnvironmentalSocialScreening.objects.get(pk=id)
        except EnvironmentalSocialScreening.DoesNotExist:
            raise Exception("EnvironmentalSocialScreening not found")
        for key, value in kwargs.items():
            setattr(form, key, value)
        form.save()
        return UpdateEnvironmentalSocialScreening(environmental_social_screening=form)

class DeleteEnvironmentalSocialScreening(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            form = EnvironmentalSocialScreening.objects.get(pk=id)
        except EnvironmentalSocialScreening.DoesNotExist:
            raise Exception("EnvironmentalSocialScreening not found")
        form.delete()
        return DeleteEnvironmentalSocialScreening(ok=True)

# --- ConsultationAndEngagement Mutations ---
class CreateConsultationAndEngagement(graphene.Mutation):
    class Arguments:
        subproject_id = Int(required=True)
        details = String(required=True)
    consultation = Field(ConsultationAndEngagementNode)
    def mutate(self, info, subproject_id, details):
        try:
            sub = Subproject.objects.get(pk=subproject_id)
        except Subproject.DoesNotExist:
            raise Exception("Subproject not found")
        cons = ConsultationAndEngagement.objects.create(subproject=sub, details=details)
        return CreateConsultationAndEngagement(consultation=cons)

class UpdateConsultationAndEngagement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        details = String()
    consultation = Field(ConsultationAndEngagementNode)
    def mutate(self, info, id, details=None):
        try:
            cons = ConsultationAndEngagement.objects.get(pk=id)
        except ConsultationAndEngagement.DoesNotExist:
            raise Exception("ConsultationAndEngagement not found")
        if details is not None:
            cons.details = details
        cons.save()
        return UpdateConsultationAndEngagement(consultation=cons)

class DeleteConsultationAndEngagement(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            cons = ConsultationAndEngagement.objects.get(pk=id)
        except ConsultationAndEngagement.DoesNotExist:
            raise Exception("ConsultationAndEngagement not found")
        cons.delete()
        return DeleteConsultationAndEngagement(ok=True)

# --- ScreeningResult Mutations ---
class CreateScreeningResult(graphene.Mutation):
    class Arguments:
        subproject_id = Int(required=True)
        risk_category = ScreeningRiskCategoryEnum(required=True)
        description = String(required=True)
        instruments_to_be_developed = String(required=True)
    screening_result = Field(ScreeningResultNode)
    def mutate(self, info, subproject_id, risk_category, description, instruments_to_be_developed):
        try:
            sub = Subproject.objects.get(pk=subproject_id)
        except Subproject.DoesNotExist:
            raise Exception("Subproject not found")
        sr = ScreeningResult.objects.create(
            subproject=sub,
            risk_category=risk_category,
            description=description,
            instruments_to_be_developed=instruments_to_be_developed
        )
        return CreateScreeningResult(screening_result=sr)

class UpdateScreeningResult(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        risk_category = ScreeningRiskCategoryEnum()
        description = String()
        instruments_to_be_developed = String()
    screening_result = Field(ScreeningResultNode)
    def mutate(self, info, id, **kwargs):
        try:
            sr = ScreeningResult.objects.get(pk=id)
        except ScreeningResult.DoesNotExist:
            raise Exception("ScreeningResult not found")
        for key, value in kwargs.items():
            setattr(sr, key, value)
        sr.save()
        return UpdateScreeningResult(screening_result=sr)

class DeleteScreeningResult(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            sr = ScreeningResult.objects.get(pk=id)
        except ScreeningResult.DoesNotExist:
            raise Exception("ScreeningResult not found")
        sr.delete()
        return DeleteScreeningResult(ok=True)

# --- PreliminaryEnvironmentalInformation Mutations ---
class CreatePreliminaryEnvironmentalInformation(graphene.Mutation):
    class Arguments:
        activity_name = String(required=True)
        activity_type = ActivityTypeEnum(required=True)
        other_activity_type = String()
        development_stage = DevelopmentStageEnum(required=True)
        other_development_stage = String()
        proponents = String()
        address = String(required=True)
        telephone = String()
        fax = String()
        mobile_phone = String()
        email = String(required=True)
        activity_location = String(required=True)
        activity_city = String(required=True)
        activity_locality = String()
        activity_district = String()
        activity_province = ProvincesEnum(required=True)
        geographic_coordinates = String()
        insertion_point = InsertionPointEnum(required=True)
        territorial_planning_framework = TerritorialPlanningFrameworkEnum(required=True)
        activity_infrastructure = String()
        associated_activities = String()
        construction_operation_technology_description = String()
        main_complementary_activities = String()
        labor_type_quantity_origin = String()
        raw_materials_type_quantity_origin_and_provenance = String()
        chemicals_used = String()
        type_origin_water_energy_consumption = String()
        fuels_lubricants_origin = String()
        other_resources_needed = String()
        land_ownership = String()
        activity_location_alternatives = String()
        brief_description_on_local_regional_ref_env_situation = String()
        physical_characteristics_of_activity_site = PyhsicalCharacteristicsEnum()
        predominant_ecosystems = PredominantEcosystemsEnum()
        location_zone = LocationZoneEnum()
        type_predominant_vegetation = TypeOfPredominantVegetationEnum()
        land_use = LandUseEnum()
        existing_infrastructure_around_activity_area = String()
        total_investment_value = Decimal()
        created_by_id = Int(required=True)
    preliminary_env_info = Field(PreliminaryEnvironmentalInformationNode)
    def mutate(self, info, activity_name, activity_type, development_stage, address,
               email, activity_location, activity_city, activity_province,
               insertion_point, territorial_planning_framework,
               physical_characteristics_of_activity_site, predominant_ecosystems,
               location_zone, type_predominant_vegetation, land_use,
               total_investment_value, created_by_id, **kwargs):
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        info_obj = PreliminaryEnvironmentalInformation.objects.create(
            activity_name=activity_name,
            activity_type=activity_type,
            development_stage=development_stage,
            address=address,
            email=email,
            activity_location=activity_location,
            activity_city=activity_city,
            activity_province=activity_province,
            insertion_point=insertion_point,
            territorial_planning_framework=territorial_planning_framework,
            physical_characteristics_of_activity_site=physical_characteristics_of_activity_site,
            predominant_ecosystems=predominant_ecosystems,
            location_zone=location_zone,
            type_predominant_vegetation=type_predominant_vegetation,
            land_use=land_use,
            total_investment_value=total_investment_value,
            created_by=created_by,
            **kwargs
        )
        return CreatePreliminaryEnvironmentalInformation(preliminary_env_info=info_obj)

class UpdatePreliminaryEnvironmentalInformation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        activity_name = String()
        email = String()
        # ... (add other fields as needed)
    preliminary_env_info = Field(PreliminaryEnvironmentalInformationNode)
    def mutate(self, info, id, **kwargs):
        try:
            info_obj = PreliminaryEnvironmentalInformation.objects.get(pk=id)
        except PreliminaryEnvironmentalInformation.DoesNotExist:
            raise Exception("PreliminaryEnvironmentalInformation not found")
        for key, value in kwargs.items():
            setattr(info_obj, key, value)
        info_obj.save()
        return UpdatePreliminaryEnvironmentalInformation(preliminary_env_info=info_obj)

class DeletePreliminaryEnvironmentalInformation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            info_obj = PreliminaryEnvironmentalInformation.objects.get(pk=id)
        except PreliminaryEnvironmentalInformation.DoesNotExist:
            raise Exception("PreliminaryEnvironmentalInformation not found")
        info_obj.delete()
        return DeletePreliminaryEnvironmentalInformation(ok=True)

# --- EmbeddedMitigation Mutations ---
class CreateEmbeddedMitigation(graphene.Mutation):
    class Arguments:
        item_number = String(required=True)
        issue = String(required=True)
        potential_impact_managed = String(required=True)
        mitigation_measure = String(required=True)
        timing = String(required=True)
        responsibility_for_implementation = String(required=True)
        means_of_verification = String(required=True)
    embedded_mitigation = Field(EmbeddedMitigationNode)
    def mutate(self, info, item_number, issue, potential_impact_managed, mitigation_measure,
               timing, responsibility_for_implementation, means_of_verification):
        em = EmbeddedMitigation.objects.create(
            item_number=item_number,
            issue=issue,
            potential_impact_managed=potential_impact_managed,
            mitigation_measure=mitigation_measure,
            timing=timing,
            responsibility_for_implementation=responsibility_for_implementation,
            means_of_verification=means_of_verification
        )
        return CreateEmbeddedMitigation(embedded_mitigation=em)

class UpdateEmbeddedMitigation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        item_number = String()
        issue = String()
        potential_impact_managed = String()
        mitigation_measure = String()
        timing = String()
        responsibility_for_implementation = String()
        means_of_verification = String()
    embedded_mitigation = Field(EmbeddedMitigationNode)
    def mutate(self, info, id, **kwargs):
        try:
            em = EmbeddedMitigation.objects.get(pk=id)
        except EmbeddedMitigation.DoesNotExist:
            raise Exception("EmbeddedMitigation not found")
        for key, value in kwargs.items():
            setattr(em, key, value)
        em.save()
        return UpdateEmbeddedMitigation(embedded_mitigation=em)

class DeleteEmbeddedMitigation(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            em = EmbeddedMitigation.objects.get(pk=id)
        except EmbeddedMitigation.DoesNotExist:
            raise Exception("EmbeddedMitigation not found")
        em.delete()
        return DeleteEmbeddedMitigation(ok=True)

# --- PlanningOrConstructionPhase Mutations ---
class CreatePlanningOrConstructionPhase(graphene.Mutation):
    class Arguments:
        item_number = String(required=True)
        issue = String(required=True)
        potential_impact_managed = String(required=True)
        mitigation_measure = String(required=True)
        timing = String(required=True)
        responsibility_for_implementation = String(required=True)
        means_of_verification = String(required=True)
    planning_phase = Field(PlanningOrConstructionPhaseNode)
    def mutate(self, info, item_number, issue, potential_impact_managed, mitigation_measure,
               timing, responsibility_for_implementation, means_of_verification):
        phase = PlanningOrConstructionPhase.objects.create(
            item_number=item_number,
            issue=issue,
            potential_impact_managed=potential_impact_managed,
            mitigation_measure=mitigation_measure,
            timing=timing,
            responsibility_for_implementation=responsibility_for_implementation,
            means_of_verification=means_of_verification
        )
        return CreatePlanningOrConstructionPhase(planning_phase=phase)

class UpdatePlanningOrConstructionPhase(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        item_number = String()
        issue = String()
        potential_impact_managed = String()
        mitigation_measure = String()
        timing = String()
        responsibility_for_implementation = String()
        means_of_verification = String()
    planning_phase = Field(PlanningOrConstructionPhaseNode)
    def mutate(self, info, id, **kwargs):
        try:
            phase = PlanningOrConstructionPhase.objects.get(pk=id)
        except PlanningOrConstructionPhase.DoesNotExist:
            raise Exception("PlanningOrConstructionPhase not found")
        for key, value in kwargs.items():
            setattr(phase, key, value)
        phase.save()
        return UpdatePlanningOrConstructionPhase(planning_phase=phase)

class DeletePlanningOrConstructionPhase(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()
    def mutate(self, info, id):
        try:
            phase = PlanningOrConstructionPhase.objects.get(pk=id)
        except PlanningOrConstructionPhase.DoesNotExist:
            raise Exception("PlanningOrConstructionPhase not found")
        phase.delete()
        return DeletePlanningOrConstructionPhase(ok=True)
    
class CreateDepartment(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        description = String()
    department = Field(DepartmentNode)
    def mutate(self, info, name, description=None):
        dept = Department.objects.create(name=name, description=description)
        return CreateDepartment(department=dept)


# --------------------------------------------------------------------
# Root Mutation and Schema
# --------------------------------------------------------------------
class Mutation(graphene.ObjectType):
    create_environ_social_assessment = CreateEnvironAndSocialRiskAndImapactAssessement.Field()
    update_environ_social_assessment = UpdateEnvironAndSocialRiskAndImapactAssessement.Field()
    delete_environ_social_assessment = DeleteEnvironAndSocialRiskAndImapactAssessement.Field()
    
    create_legal_requirement_control = CreateLegalRequirementControl.Field()
    update_legal_requirement_control = UpdateLegalRequirementControl.Field()
    delete_legal_requirement_control = DeleteLegalRequirementControl.Field()
    
    create_contact_person = CreateContactPerson.Field()
    update_contact_person = UpdateContactPerson.Field()
    delete_contact_person = DeleteContactPerson.Field()
    
    create_biodeversidade = CreateBiodeversidadeRecursosNaturais.Field()
    update_biodeversidade = UpdateBiodeversidadeRecursosNaturais.Field()
    delete_biodeversidade = DeleteBiodeversidadeRecursosNaturais.Field()
    
    create_subproject = CreateSubproject.Field()
    update_subproject = UpdateSubproject.Field()
    delete_subproject = DeleteSubproject.Field()
    
    create_environmental_social_screening = CreateEnvironmentalSocialScreening.Field()
    update_environmental_social_screening = UpdateEnvironmentalSocialScreening.Field()
    delete_environmental_social_screening = DeleteEnvironmentalSocialScreening.Field()
    
    create_consultation = CreateConsultationAndEngagement.Field()
    update_consultation = UpdateConsultationAndEngagement.Field()
    delete_consultation = DeleteConsultationAndEngagement.Field()
    
    create_screening_result = CreateScreeningResult.Field()
    update_screening_result = UpdateScreeningResult.Field()
    delete_screening_result = DeleteScreeningResult.Field()
    
    create_preliminary_env_info = CreatePreliminaryEnvironmentalInformation.Field()
    update_preliminary_env_info = UpdatePreliminaryEnvironmentalInformation.Field()
    delete_preliminary_env_info = DeletePreliminaryEnvironmentalInformation.Field()
    
    create_embedded_mitigation = CreateEmbeddedMitigation.Field()
    update_embedded_mitigation = UpdateEmbeddedMitigation.Field()
    delete_embedded_mitigation = DeleteEmbeddedMitigation.Field()
    
    create_planning_phase = CreatePlanningOrConstructionPhase.Field()
    update_planning_phase = UpdatePlanningOrConstructionPhase.Field()
    delete_planning_phase = DeletePlanningOrConstructionPhase.Field()

    create_department = CreateDepartment.Field()

class RiskManagementStatus(graphene.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

schema = graphene.Schema(query=Query, mutation=Mutation)
