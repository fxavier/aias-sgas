from django.db import models
from users.models import User
from core.utils.utils import law_file_path



class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Duration(models.TextChoices):
    CURTO_PRAZO = 'CURTO_PRAZO', 'Curto Prazo'
    MEDIO_PRAZO = 'MEDIO_PRAZO', 'Médio Prazo'
    LONGO_PRAZO = 'LONGO_PRAZO', 'Longo Prazo'

class EnvironmentalFactor(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Extension(models.TextChoices):
    LOCAL = 'LOCAL', 'Local'
    REGIONAL = 'REGIONAL', 'Regional'
    NACIONAL = 'NACIONAL', 'Nacional'
    GLOBAL = 'GLOBAL', 'Global'

class Intensity(models.TextChoices):
    BAIXA = 'BAIXA', 'Baixa'
    MEDIA = 'MEDIA', 'Média'
    ALTA = 'ALTA', 'Alta'

class LifeCycle(models.TextChoices):
    PRE_CONSTRUCAO = 'PRE_CONSTRUCAO', 'Pré-Construção'
    CONSTRUCAO = 'CONSTRUCAO', 'Construção'
    OPERACAO = 'OPERACAO', 'Operação'
    DESATIVACAO = 'DESATIVACAO', 'Desativação'
    ENCERRAMENTO = 'ENCERRAMENTO', 'Encerramento'
    REINTEGRACAO_RESTAURACAO = 'REINTEGRACAO_RESTAURACAO', 'Reintegração/Restauração'

class Probability(models.TextChoices):
    IMPROVAVEL = 'IMPROVAVEL', 'Improvável'
    PROVAVEL = 'PROVAVEL', 'Provável'
    ALTAMENTE_PROVAVEL = 'ALTAMENTE_PROVAVEL', 'Altamente Provável'
    DEFINITIVA = 'DEFINITIVA', 'Definitiva'

class ResponseType(models.TextChoices):
    SIM = 'SIM', 'Sim'
    NAO = 'NAO', 'Não'

class RisksAndImpact(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Statute(models.TextChoices):
    POSITIVO = 'POSITIVO', 'Positivo'
    NEGATIVO = 'NEGATIVO', 'Negativo'

class Status(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    REVOKED = 'REVOKED', 'Revoked'
    AMENDED = 'AMENDED', 'Amended'

class EnvironAndSocialRiskAndImapactAssessement(models.Model):
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    risks_and_impact = models.ForeignKey(RisksAndImpact, on_delete=models.CASCADE)
    environmental_factor = models.ForeignKey(EnvironmentalFactor, on_delete=models.CASCADE)
    life_cycle = models.CharField(max_length=50, choices=LifeCycle.choices)
    statute = models.CharField(max_length=50, choices=Statute.choices)
    extension = models.CharField(max_length=50, choices=Extension.choices)
    duration = models.CharField(max_length=50, choices=Duration.choices)
    intensity = models.CharField(max_length=50, choices=Intensity.choices)
    probability = models.CharField(max_length=50, choices=Probability.choices)
    significance = models.CharField(max_length=255, null=True, blank=True, editable=False)
    description_of_measures = models.TextField()
    deadline = models.CharField(max_length=255)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible')
    effectiveness_assessment = models.TextField()
    legal_requirements = models.ManyToManyField('LegalRequirementControl', related_name='legal_requirements')
    compliance_requirements = models.TextField()   
    observations = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='environ_and_social_risks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity
    class Meta:
        verbose_name = 'Environmental and Social Risk and Impact Assessement (FR.AS.002)'
        verbose_name_plural = 'Environmental and Social Risks and Impact Assessements (FR.AS.002)'


class LegalRequirementControl(models.Model):
    number = models.CharField(max_length=255)
    document_title = models.CharField(max_length=255)
    effective_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=Status.choices)
    amended_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    observation = models.TextField(null=True, blank=True)
    law_file = models.FileField(upload_to=law_file_path, null=True, blank=True) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='legal_requirements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_title
    
    class Meta:
        verbose_name = 'Legal Requirement Control (FR.AS.003)'
        verbose_name_plural = 'Legal Requirements Control (FR.AS.003)'


# BEGIN OF FORMULARIO DE TRIAGEM AMBIENTAL E SOCIAL FR.AS.023

class ContactPerson(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date = models.DateField()
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
class ResponsibleForFillingForm(ContactPerson):
    pass

    def __str__(self):
        return self.name
    
class ResponsibleForVerification(ContactPerson):
    pass

    def __str__(self):
        return self.name
    
class BiodeversidadeRecursosNaturais(models.Model):
    reference = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Biodiversidade e Recursos Naturais'
        verbose_name_plural = 'Biodiversidade e Recursos Naturais'

    def __str__(self):
        return self.description
    

class Subproject(models.Model):
    name = models.CharField(max_length=255)
    contract_reference = models.CharField(max_length=255, blank=True, null=True)
    contractor_name = models.CharField(max_length=255, blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255)
    geographic_coordinates = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255)
    approximate_area = models.TextField()

    def __str__(self):
        return self.name

class EnvironmentalSocialScreening(models.Model):
    responsible_for_filling_form = models.ForeignKey(ResponsibleForFillingForm, on_delete=models.CASCADE, related_name='risks')
    responsible_for_verification = models.ForeignKey(ResponsibleForVerification, on_delete=models.CASCADE, related_name='risks')
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='risks')
    biodiversidade_recursos_naturais = models.ForeignKey(BiodeversidadeRecursosNaturais, on_delete=models.CASCADE)
    response = models.CharField(max_length=100, choices=ResponseType.choices)
    comment = models.TextField(blank=True, null=True)
    relevant_standard = models.CharField(max_length=255, blank=True, null=True)
    consultation_and_engagement = models.TextField(blank=True, null=True)
    recomended_actions = models.TextField(blank=True, null=True)
    screening_results = models.ForeignKey('ScreeningResult', on_delete=models.CASCADE, related_name='screening_results')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='risks_assessement')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subproject.name
    class Meta:
        verbose_name = 'Environmental and Social Screening Form (FR.AS.023)'
        verbose_name_plural = 'Environmental and Social Screening Forms (FR.AS.023)'

class ConsultationAndEngagement(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='consultations')
    details = models.TextField()

    def __str__(self):
        return f"Consultation for {self.subproject.name}"

class ScreeningResult(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='screening_results')
    RISK_CHOICES = [
        ('ALTO', 'Alto Risco'),
        ('SUBSTANCIAL', 'Risco Substancial'),
        ('MODERADO', 'Risco Moderado'),
        ('BAIXO', 'Risco Baixo')
    ]
    risk_category = models.CharField(max_length=15, choices=RISK_CHOICES)
    description = models.TextField()
    instruments_to_be_developed = models.TextField()

    def __str__(self):
        return f"Screening Result for {self.subproject.name}"
    
# END OF FORMULARIO DE TRIAGEM AMBIENTAL E SOCIAL FR.AS.023


# BEGIN OF FICHA DE INFORMAÇÃO AMBIENTAL PRELIMINAR MOD.AS.02
 
class Provinces(models.TextChoices):
    MAPUTO = 'MAPUTO', 'Maputo'
    MAPUTO_CITY = 'MAPUTO_CITY', 'Maputo City'
    GAZA = 'GAZA', 'Gaza'
    INHAMBANE = 'INHAMBANE', 'Inhambane'
    SOFALA = 'SOFALA', 'Sofala'
    MANICA = 'MANICA', 'Manica'
    TETE = 'TETE', 'Tete'
    ZAMBEZIA = 'ZAMBEZIA', 'Zambezia'
    NAMPULA = 'NAMPULA', 'Nampula'
    CABO_DELGADO = 'CABO_DELGADO', 'Cabo Delgado'
    NIASSA = 'NIASSA', 'Niassa'

class ActivityType(models.TextChoices):
    TURISTICA = 'TURISTICA', 'Turística'
    INDUSTRIAL = 'INDUSTRIAL', 'Industrial'
    AGRO_PECUARIA = 'AGRO_PECUARIA', 'Agro-Pecuária'
    ENERGETICA = 'ENERGETICA', 'Energética'
    SERVICOS = 'SERVICOS', 'Serviços'
    OUTRA = 'OUTRA', 'Outra'


class DevelopmentStage(models.TextChoices):
    NOVA = 'NOVA', 'Nova'
    REABILITACAO = 'REABILITACAO', 'Reabilitação'
    EXPANSAO = 'EXPANSAO', 'Expansão'
    OUTRO = 'OUTRO', 'Outro'

class InsertionPoint(models.TextChoices):
    RURAL = 'RURAL', 'Rural'
    URBANO = 'URBANO', 'Urbano'
    PERIURBANO = 'PERIURBANO', 'Periurbano'

class TerritorialPlanningFramework(models.TextChoices):
    ESPACO_HABITACIONAL = 'ESPACO_HABITACIONAL', 'Espaço Habitacional'
    INDUSTRIAL = 'INDUSTRIAL', 'Industrial'
    SERVICOS = 'SERVICOS', 'Serviços'
    OUTRO = 'OUTRO', 'Outro'

class PyhsicalCharacteristics(models.TextChoices):
    PLANICIE = 'PLANICIE', 'Planície'
    PLANALTO = 'PLANALTO', 'Planalto'
    VALE = 'VALE', 'Vale'
    MONTANHA = 'MONTANHA', 'Montanha'

class PredominantEcosystems(models.TextChoices):
    FLUVIAL = 'FLUVIAL', 'Fluvial'
    LACUSTRE = 'LACUSTRE', 'Lacustre'
    MARINHO = 'MARINHO', 'Marinho'
    TERRESTRE = 'TERRESTRE', 'Terrestre'

class LocationZone(models.TextChoices):
    COSTEIRA = 'COSTEIRA', 'Costeira'
    INTERIOR = 'INTERIOR', 'Interior'
    ILHA = 'ILHA', 'Ilha'

class TypeOfPredominantVegetation(models.TextChoices):
    FLORESTA = 'FLORESTA', 'Floresta'
    SAVANA = 'SAVANA', 'Savana'
    OUTRO = 'OUTRO', 'Outro'

class LandUse(models.TextChoices):
    AGROPECUARIO = 'AGROPECUARIO', 'Agropecuário'
    HABITACIONAL = 'HABITACIONAL', 'Habitacional'
    INDUSTRIAL = 'INDUSTRIAL', 'Industrial'
    PROTECCAO = 'PROTECCAO', 'Proteção'
    OUTRO = 'OUTRO', 'Outro'
class PreliminaryEnvironmentalInformation(models.Model):
    activity_name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255, choices=ActivityType.choices)
    other_activity_type = models.CharField(max_length=255, blank=True, null=True)
    development_stage = models.CharField(max_length=255, choices=DevelopmentStage.choices)
    other_development_stage = models.CharField(max_length=255, blank=True, null=True)
    proponents = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    activity_location = models.CharField(max_length=255)
    activity_city = models.CharField(max_length=255)
    activity_locality = models.CharField(max_length=255, null=True, blank=True)
    activity_district = models.CharField(max_length=255, null=True, blank=True)
    activity_province = models.CharField(max_length=255, choices=Provinces.choices)
    geographic_coordinates = models.TextField(blank=True, null=True)
    insertion_point = models.CharField(max_length=255, choices=InsertionPoint.choices)
    territorial_planning_framework = models.CharField(max_length=255, choices=TerritorialPlanningFramework.choices)
    activity_infrastructure = models.TextField(null=True, blank=True)
    associated_activities = models.TextField(null=True, blank=True)
    construction_operation_technology_description = models.TextField(null=True, blank=True)
    main_complementary_activities = models.TextField(null=True, blank=True)
    labor_type_quantity_origin = models.TextField(null=True, blank=True)
    raw_materials_type_quantity_origin_and_provenance = models.TextField(null=True, blank=True)
    chemicals_used = models.TextField(null=True, blank=True)
    type_origin_water_energy_consumption = models.TextField(null=True, blank=True)
    fuels_lubricants_origin = models.TextField(null=True, blank=True)
    other_resources_needed = models.TextField(null=True, blank=True)
    land_ownership = models.TextField(null=True, blank=True)
    activity_location_alternatives = models.TextField(null=True, blank=True)
    brief_description_on_local_regional_ref_env_situation = models.TextField(null=True, blank=True)
    physical_characteristics_of_activity_site = models.TextField(choices=PyhsicalCharacteristics.choices, null=True, blank=True)
    predominant_ecosystems = models.TextField(null=True, blank=True, choices=PredominantEcosystems.choices)
    location_zone = models.TextField(null=True, blank=True, choices=LocationZone.choices)
    type_predominant_vegetation = models.TextField(null=True, blank=True, choices=TypeOfPredominantVegetation.choices)
    land_use = models.TextField(null=True, blank=True, choices=LandUse.choices)
    existing_infrastructure_around_activity_area = models.TextField(null=True, blank=True)
    total_investment_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preliminar_infos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_name
    
    class Meta:
        verbose_name = 'Preliminary Environmental Information Form (MOD.AS.02)'
        verbose_name_plural = 'Preliminary Environmental Information Forms (MOD.AS.02)'


# END OF FICHA DE INFORMAÇÃO AMBIENTAL PRELIMINAR MOD.AS.02