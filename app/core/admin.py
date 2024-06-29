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
     PreliminaryEnvironmentalInformation
)
from riskmanagement.forms import EnvironmentalSocialScreeningForm   
from extcommungrievancemechanism.forms import ComplaintAndClaimRecordForm
from extcommungrievancemechanism.models import (
    ClaimNonComplianceControl, ComplaintAndClaimRecord, PhotoDocumentProvingClosure,
    ClaimComplainControl
)   

from emergencyresponse.models import (
    PessoaEnvolvida, PessoasEnvolvidasNaInvestigacao,
    AccoesImediatasECorrectivas, RelatorioAcidenteIncidente,
    ListaVerificacaoKitPrimeirosSocorros
)

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


admin.site.site_header = 'SGAS - Sistema de gestão ambiental e social'
