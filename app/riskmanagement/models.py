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

class Arias(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity


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

    def __str__(self):
        return self.document_title


# BEGIN OF FORMULARIO DE TRIAGEM AMBIENTAL E SOCIAL FR.AS.023
class ContactPerson(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date = models.DateField()
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

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

class EnvironmentalSocialRisk(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='risks')
    reference = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    response = models.CharField(max_length=100, choices=ResponseType.choices)
    comment = models.TextField(blank=True, null=True)
    relevant_standard = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.reference} - {self.description}"

class ConsultationEngagement(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='consultations')
    details = models.TextField()

    def __str__(self):
        return f"Consultation for {self.subproject.name}"

class ProposedAction(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name='proposed_actions')
    question_reference = models.CharField(max_length=255)
    recommended_action = models.TextField()

    def __str__(self):
        return f"Action for {self.question_reference}"

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

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('TURISTICA', 'Turística'),
        ('INDUSTRIAL', 'Industrial'),
        ('AGRO_PECUARIA', 'Agro-Pecuária'),
        ('ENERGETICA', 'Energética'),
        ('SERVICOS', 'Serviços'),
        ('OUTRA', 'Outra'),
    ]

    DEVELOPMENT_STAGES = [
        ('NOVA', 'Nova'),
        ('REABILITACAO', 'Reabilitação'),
        ('EXPANSAO', 'Expansão'),
        ('OUTRO', 'Outro'),
    ]

    name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    other_activity_type = models.CharField(max_length=255, blank=True, null=True)
    development_stage = models.CharField(max_length=50, choices=DEVELOPMENT_STAGES)
    other_development_stage = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Proponent(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='proponents')
    name = models.CharField(max_length=255)
    address = models.TextField()
    telephone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Location(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='locations')
    neighborhood = models.CharField(max_length=255)
    province = models.CharField(max_length=100, choices=Provinces.choices)
    district = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    geographic_coordinates = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.province}"

class ActivityDescription(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='descriptions')
    infrastructure = models.TextField()
    associated_activities = models.TextField()
    construction_technology = models.TextField()
    main_complementary_activities = models.TextField()
    labor_type_quantity = models.TextField()
    raw_materials_type_quantity = models.TextField()
    chemicals_used = models.TextField(blank=True, null=True)
    water_energy_consumption = models.TextField()
    fuels_lubricants = models.TextField()
    other_resources = models.TextField()

    def __str__(self):
        return f"Description for {self.activity.name}"

class LandOwnership(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='land_ownership')
    legal_status = models.TextField()

    def __str__(self):
        return f"Land Ownership for {self.activity.name}"

class AlternativeLocations(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='alternative_locations')
    reason_for_choice = models.TextField()
    alternative1 = models.TextField()
    alternative2 = models.TextField()

    def __str__(self):
        return f"Alternatives for {self.activity.name}"

class EnvironmentalSituation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='environmental_situation')
    physical_characteristics = models.TextField()
    predominant_ecosystems = models.TextField()
    location_zone = models.TextField()
    predominant_vegetation = models.TextField()
    land_use = models.TextField()
    existing_infrastructure = models.TextField()

    def __str__(self):
        return f"Environmental Situation for {self.activity.name}"

class Investment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='investments')
    total_investment_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Investment for {self.activity.name}"

# END OF FICHA DE INFORMAÇÃO AMBIENTAL PRELIMINAR MOD.AS.02