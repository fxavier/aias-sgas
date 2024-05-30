from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin
from riskmanagement.models import (
     Department, EnvironmentalFactor, RisksAndImpact, Arias, LegalRequirementControl,
     ContactPerson, Subproject, EnvironmentalSocialRisk, ConsultationEngagement,
     ProposedAction, ScreeningResult, Activity, Proponent, Location, ActivityDescription,
     LandOwnership, AlternativeLocations, EnvironmentalSituation, Investment
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

class EnvironmentalFactorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'description']

class RisksAndImpactAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'description',]

class AriasAdmin(ImportExportMixin, admin.ModelAdmin):
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

class LegalRequirementControlAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
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

class ContactPersonAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'role',
        'contact',
        'date',
        'signature',
    ]

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

class EnvironmentalSocialRiskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'subproject',
        'reference',
        'description',
        'response',
        'relevant_standard',
    ]

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
class ActivityAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'activity_type',
        'other_activity_type',
        'development_stage',
        'other_development_stage',

    ]
class ProponentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'name',
        'address',
        'telephone',
        'fax',
        'mobile',
        'email',
    ]

class LocationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'neighborhood',
        'province',
        'district',
        'city',
        'geographic_coordinates',
    ]

class ActivityDescriptionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'infrastructure',
        'associated_activities',
        'construction_technology',
        'main_complementary_activities',
        'labor_type_quantity',
        'raw_materials_type_quantity',
        'chemicals_used',
        'water_energy_consumption',
        'fuels_lubricants',
        'other_resources',
    ]

class LandOwnershipAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'legal_status',
    ]

class AlternativeLocationsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'reason_for_choice',
        'alternative1',
        'alternative2',
    ]

class EnvironmentalSituationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'activity',
        'physical_characteristics',
        'predominant_ecosystems',
        'location_zone',
        'predominant_vegetation',
        'land_use',
        'existing_infrastructure',
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(EnvironmentalFactor, EnvironmentalFactorAdmin)
admin.site.register(RisksAndImpact, RisksAndImpactAdmin)
admin.site.register(Arias, AriasAdmin)
admin.site.register(LegalRequirementControl, LegalRequirementControlAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Subproject, SubprojectAdmin)
admin.site.register(EnvironmentalSocialRisk, EnvironmentalSocialRiskAdmin)
admin.site.register(ConsultationEngagement, ConsultationEngagementAdmin)
admin.site.register(ProposedAction, ProposedActionAdmin)
admin.site.register(ScreeningResult, ScreeningResultAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Proponent, ProponentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ActivityDescription, ActivityDescriptionAdmin)
admin.site.register(LandOwnership, LandOwnershipAdmin)
admin.site.register(AlternativeLocations, AlternativeLocationsAdmin)
admin.site.register(EnvironmentalSituation, EnvironmentalSituationAdmin)

admin.site.site_header = 'SGAS - Sistema de gestão ambiental e social'
