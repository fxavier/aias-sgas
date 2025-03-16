from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin
from riskmanagement.models import (
     Department, EnvironmentalFactor, RisksAndImpact, LegalRequirementControl,
     ResponsibleForFillingForm, ResponsibleForVerification, Subproject,
     EnvironmentalSocialScreening, EnvironAndSocialRiskAndImapactAssessement,
     ScreeningResult, BiodeversidadeRecursosNaturais,
     PreliminaryEnvironmentalInformation, EmbeddedMitigation, PlanningOrConstructionPhase
)
from riskmanagement.forms import EnvironmentalSocialScreeningForm   
from extcommungrievancemechanism.forms import ComplaintAndClaimRecordForm
from extcommungrievancemechanism.models import (
    ClaimNonComplianceControl, ComplaintAndClaimRecord, PhotoDocumentProvingClosure,
    ClaimComplainControl, WorkerGrievance
)   

from emergencyresponse.models import (
    PessoaEnvolvida, PessoasEnvolvidasNaInvestigacao,
    AccoesImediatasECorrectivas, RelatorioAcidenteIncidente,
    ListaVerificacaoKitPrimeirosSocorros, Incidents, IncidentFlashReport
)

from documentmanagement.models import DocumentType, Document

from programsmanagement.models import StrategicObjective, SpecificObjective

from organizationalcapacityandcompetency.models import (
    TrainingNeeds, TrainingPlan, TrainingEffectivnessAssessment,
    TrainingEvaluationQuestions, Position, Training, ToolBoxTalks, TrainingMatrix,
    AcceptanceConfirmation, OHSACTING
)

from reportingmonitoringandreview.models import (
    WasteTransferLog
)

from resourceefficiencyandpollutionprevention.models import (
    WastManagement
)

from app.admin import custom_admin_site

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    sortable_by = ['id']

class EnvironmentalFactorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'description']
    sortable_by = ['id']
    

class RisksAndImpactAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'description',]
    sortable_by = ['id']

class EnvironAndSocialRiskAndImapactAssessementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'departament',
        'activity',
        'risks_and_impact',
        'environmental_factor',
        'life_cycle',
        'statute',
        'extension',
        'duration',
        'intensity',
        'probability',
        'significance',
        'description_of_measures',
        'deadline',
        'effectiveness_assessment',
      #  'legal_requirements',
        'compliance_requirements',
        'observations',
        'responsible',
        'created_at',
    
    ]
    sortable_by = ['id']

class LegalRequirementControlAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'number',
        'document_title',
        'effective_date',
        'description',
        'status',
        'amended_description',
        'created_at',
        'updated_at',
        'law_file',
    ]
    sortable_by = ['id']
class ResponsibleFoFillingAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'role',
        'contact',
        'date',
        'signature',
    ]
    sortable_by = ['name']
class ResponsibleForVerificationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'role',
        'contact',
        'date',
        'signature',
    ]
    sortable_by = ['name']

class SubprojectAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'contract_reference',
        'contractor_name',
        'estimated_cost',
        'location',
        'geographic_coordinates',
        'type',
        'approximate_area',
    ]
    sortable_by = ['name']

class BiodeversidadeRecursosNaturaisAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'reference',
        'description',
    ]
    sortable_by = ['id']
class EnvironmentalSocialScreeningAdmin(ImportExportMixin, admin.ModelAdmin):
    form = EnvironmentalSocialScreeningForm
    list_display = [
        'subproject',
        'biodiversidade_recursos_naturais',
        'response',
        'relevant_standard',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['recomended_actions'].hidden = True
        return form
    

class ConsultationEngagementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'subproject',
        'details',
    ]

class ProposedActionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'subproject',
        'question_reference',
        'recommended_action',
    ]

class ScreeningResultAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'subproject',
        'risk_category',
        'description',
    ]

class PreliminaryEnvironmentalInformationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity_name',
        'activity_type',
        'other_activity_type',
        'development_stage',
        'other_development_stage'
    ]

class ClaimNonComplianceControlAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [ 
        'number',
        'department',
        'non_compliance_description',
        'identified_causes',
        'corrective_actions',
        'responsible_person',
        'deadline',
        'status',
        'effectiveness_evaluation',
        'responsible_person_evaluation',
        'observation'
    ]

class ComplaintAndClaimAdmin(ImportExportMixin, admin.ModelAdmin):
    form = ComplaintAndClaimRecordForm
    list_display = [
        'number',
        'date_occurred',
        'local_occurrence',
        'how_occurred',
        'who_involved',
        'report_and_explanation',
        'claim_local_occurrence'
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['action_taken'].hidden = True
        form.base_fields['notification_method'].hidden = True
        form.base_fields['other_claim_category'].hidden = True
        return form

class ClaimComplainControlAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'number',
        'claim_complain_submitted_by',
        'claim_complain_reception_date',
        'claim_complain_description',
        'treatment_action',
        'claim_complain_responsible_person',
        'claim_complain_deadline',
        'claim_complain_status',
        'closure_date',
        'observation'
    ]

class PessoaEnvolvidaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'nome',
        'departamento',
        'outras_informacoes',
    ]

class PessoasEnvolvidasNaInvestigacaoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'nome',
        'empresa',
        'actividade',
        'assinatura',
        'data',
    ]

class AccoesImediatasECorrectivasAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'accao',
        'descricao',
        'responsavel',
        'data',
        'assinatura',
    ]

class RelatorioAcidenteIncidenteAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'nome',
        'funcao',
        'departamento',
        'data',
        'hora',
        'local',
        'actividade_em_curso',
        'descricao_do_acidente',
        'tipo_de_incidente',
    ] 

class ListaVerificacaoKitPrimeirosSocorrosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'descricao',
        'quantidade',
        'data',
        'prazo',
        'observacao',
        'inspecao_realizada_por',
       
    ]

class DocumentTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'description',
    ]

class DocumentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'code',
        'creation_date',
        'revision_date',
        'document_name',
        'document_type',
        'document_path',
        'document_state',
        'retention_period',
        'disposal_method',
        'observation',
    ]
    search_fields = ('code', 'document_name', 'document_type__description')
    list_filter = ('id', 'code', 'document_name', 'document_type')

class WorkerGrievanceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'company',
        'date',
        'prefered_contact_method',
        'contact',
        'grievance_details', 
    ]

class StrategicObjectiveAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'description',
        'goals',
        'strategies_for_achievement',
    ]

class SpecificObjectiveAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'strategic_objective',
        'specific_objective',
        'actions_for_achievement',
        'responsible_person',
        'necessary_resources',
        'indicator',
        'goal',
        'monitoring_frequency',
        'deadline',
        'observation',
    ]

class TrainingNeedsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
    'filled_by',
    'date',
    'department',
    'training',
    'training_objective',
    'proposal_of_training_entity',
    'potential_training_participants',
    ]

class TrainingPlanAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'updated_by',
        'date',
        'year',
        'training_area',
        'training_title',
        'training_objective',
        'training_type',
        'training_entity',
        'duration',
        'number_of_trainees',
        'training_recipients',
        'training_month',
        'training_status',
        'observations',
    ]

class TrainingEffectivnessAssessmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'training',
        'date',
        'department',
        'trainee',
        'immediate_supervisor',
        'training_evaluation_question',
        'answer',
        'human_resource_evaluation',
    ]

class TrainingEvaluationQuetionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'question',
    ]

class PositionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class TrainingAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class ToolBoxTalksAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class TrainingMatrixAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'date',
        'position',
        'training',
        'toolbox_talks',
        'effectiveness',
        'actions_training_not_effective',
    ]

class AcceptanceConfirmationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'description',
    ]

class OHSACTINGAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'fullname',
        'designation',
        'terms_of_office_from',
        'terms_of_office_to',
        'acceptance_confirmation_display',
    ]

    def acceptance_confirmation_display(self, obj):
        return ", ".join([str(item) for item in obj.acceptance_confirmation.all()])
    acceptance_confirmation_display.short_description = 'Acceptance Confirmation'

class IncidentsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'description'
    ]

class IncidentFlashReportAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'incidents_display',
        'date_incident',
        'time_incident',
        'section',
        'location_incident',
        'date_reported'
    ]

    def incidents_display(self, obj):
        return ", ".join([str(item) for item in obj.incidents.all()])
    incidents_display.short_description = 'Incidents'

class EmbeddedMitigationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
       'item_number',
       'issue',
       'potential_impact_managed',
       'mitigation_measure',
       'timing',
       'responsibility_for_implementation',
       'means_of_verification'
    ]

class PlanningOrConstructionPhaseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'item_number',
        'issue',
        'potential_impact_managed',
        'mitigation_measure',
        'timing',
        'responsibility_for_implementation',
        'means_of_verification'
    ]

class WasteTranferLogAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'waste_type',
        'how_is_waste_contained',
        'how_much_waste',
        'reference_number',
        'date_of_removal',
        'transfer_company',
        'special_instructions'
    ]

class WasteManagementadmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'waste_route',
        'labelling',
        'storage',
        'transportation_company_method',
        'disposal_company',
        'special_instructions'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(EnvironmentalFactor, EnvironmentalFactorAdmin)
admin.site.register(RisksAndImpact, RisksAndImpactAdmin)
admin.site.register(EnvironAndSocialRiskAndImapactAssessement, EnvironAndSocialRiskAndImapactAssessementAdmin)
admin.site.register(LegalRequirementControl, LegalRequirementControlAdmin)
admin.site.register(ResponsibleForFillingForm, ResponsibleFoFillingAdmin)
admin.site.register(ResponsibleForVerification, ResponsibleForVerificationAdmin)
admin.site.register(Subproject, SubprojectAdmin)
admin.site.register(EnvironmentalSocialScreening, EnvironmentalSocialScreeningAdmin)
admin.site.register(ScreeningResult, ScreeningResultAdmin)
admin.site.register(BiodeversidadeRecursosNaturais, BiodeversidadeRecursosNaturaisAdmin)
admin.site.register(PreliminaryEnvironmentalInformation, PreliminaryEnvironmentalInformationAdmin)
admin.site.register(ClaimNonComplianceControl, ClaimNonComplianceControlAdmin)
admin.site.register(ComplaintAndClaimRecord, ComplaintAndClaimAdmin)
admin.site.register(PhotoDocumentProvingClosure)
admin.site.register(ClaimComplainControl, ClaimComplainControlAdmin)
admin.site.register(PessoaEnvolvida, PessoaEnvolvidaAdmin)
admin.site.register(PessoasEnvolvidasNaInvestigacao, PessoasEnvolvidasNaInvestigacaoAdmin)
admin.site.register(AccoesImediatasECorrectivas, AccoesImediatasECorrectivasAdmin)
admin.site.register(RelatorioAcidenteIncidente, RelatorioAcidenteIncidenteAdmin)
admin.site.register(ListaVerificacaoKitPrimeirosSocorros, ListaVerificacaoKitPrimeirosSocorrosAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(WorkerGrievance, WorkerGrievanceAdmin)
admin.site.register(StrategicObjective, StrategicObjectiveAdmin)
admin.site.register(SpecificObjective, SpecificObjectiveAdmin)
admin.site.register(TrainingNeeds, TrainingNeedsAdmin)
admin.site.register(TrainingPlan, TrainingPlanAdmin)
admin.site.register(TrainingEffectivnessAssessment, TrainingEffectivnessAssessmentAdmin)
admin.site.register(TrainingEvaluationQuestions, TrainingEvaluationQuetionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(ToolBoxTalks, ToolBoxTalksAdmin)
admin.site.register(TrainingMatrix, TrainingMatrixAdmin)
admin.site.register(AcceptanceConfirmation, AcceptanceConfirmationAdmin)
admin.site.register(OHSACTING, OHSACTINGAdmin)
admin.site.register(Incidents, IncidentsAdmin)
admin.site.register(IncidentFlashReport, IncidentFlashReportAdmin)
admin.site.register(EmbeddedMitigation, EmbeddedMitigationAdmin)
admin.site.register(PlanningOrConstructionPhase, PlanningOrConstructionPhaseAdmin)
admin.site.register(WasteTransferLog, WasteTranferLogAdmin)
admin.site.register(WastManagement, WasteManagementadmin)


custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Department, DepartmentAdmin)
custom_admin_site.register(EnvironmentalFactor, EnvironmentalFactorAdmin)
custom_admin_site.register(RisksAndImpact, RisksAndImpactAdmin)
custom_admin_site.register(EnvironAndSocialRiskAndImapactAssessement, EnvironAndSocialRiskAndImapactAssessementAdmin)
custom_admin_site.register(LegalRequirementControl, LegalRequirementControlAdmin)
custom_admin_site.register(ResponsibleForFillingForm, ResponsibleFoFillingAdmin)
custom_admin_site.register(ResponsibleForVerification, ResponsibleForVerificationAdmin)
custom_admin_site.register(Subproject, SubprojectAdmin)
custom_admin_site.register(EnvironmentalSocialScreening, EnvironmentalSocialScreeningAdmin)
custom_admin_site.register(ScreeningResult, ScreeningResultAdmin)
custom_admin_site.register(BiodeversidadeRecursosNaturais, BiodeversidadeRecursosNaturaisAdmin)
custom_admin_site.register(PreliminaryEnvironmentalInformation, PreliminaryEnvironmentalInformationAdmin)
custom_admin_site.register(ClaimNonComplianceControl, ClaimNonComplianceControlAdmin)
custom_admin_site.register(ComplaintAndClaimRecord, ComplaintAndClaimAdmin)
custom_admin_site.register(PhotoDocumentProvingClosure)
custom_admin_site.register(ClaimComplainControl, ClaimComplainControlAdmin)
custom_admin_site.register(PessoaEnvolvida, PessoaEnvolvidaAdmin)
custom_admin_site.register(PessoasEnvolvidasNaInvestigacao, PessoasEnvolvidasNaInvestigacaoAdmin)
custom_admin_site.register(AccoesImediatasECorrectivas, AccoesImediatasECorrectivasAdmin)
custom_admin_site.register(RelatorioAcidenteIncidente, RelatorioAcidenteIncidenteAdmin)
custom_admin_site.register(ListaVerificacaoKitPrimeirosSocorros, ListaVerificacaoKitPrimeirosSocorrosAdmin)
custom_admin_site.register(DocumentType, DocumentTypeAdmin)
custom_admin_site.register(Document, DocumentAdmin)
custom_admin_site.register(WorkerGrievance, WorkerGrievanceAdmin)
custom_admin_site.register(StrategicObjective, StrategicObjectiveAdmin)
custom_admin_site.register(SpecificObjective, SpecificObjectiveAdmin)
custom_admin_site.register(TrainingNeeds, TrainingNeedsAdmin)
custom_admin_site.register(TrainingPlan, TrainingPlanAdmin)
custom_admin_site.register(TrainingEffectivnessAssessment, TrainingEffectivnessAssessmentAdmin)
custom_admin_site.register(TrainingEvaluationQuestions, TrainingEvaluationQuetionAdmin)
custom_admin_site.register(Position, PositionAdmin)
custom_admin_site.register(Training, TrainingAdmin)
custom_admin_site.register(ToolBoxTalks, ToolBoxTalksAdmin)
custom_admin_site.register(TrainingMatrix, TrainingMatrixAdmin)
custom_admin_site.register(AcceptanceConfirmation, AcceptanceConfirmationAdmin)
custom_admin_site.register(OHSACTING, OHSACTINGAdmin)
custom_admin_site.register(Incidents, IncidentsAdmin)
custom_admin_site.register(IncidentFlashReport, IncidentFlashReportAdmin)
custom_admin_site.register(EmbeddedMitigation, EmbeddedMitigationAdmin)
custom_admin_site.register(PlanningOrConstructionPhase, PlanningOrConstructionPhaseAdmin)
custom_admin_site.register(WasteTransferLog, WasteTranferLogAdmin)
custom_admin_site.register(WastManagement, WasteManagementadmin)


# admin.site.site_header = 'SGAS - Sistema de gestão ambiental e social'
