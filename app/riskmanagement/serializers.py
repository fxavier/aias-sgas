from rest_framework import serializers
from riskmanagement.models import (
    Department, EnvironmentalFactor, RisksAndImpact, EnvironAndSocialRiskAndImapactAssessement,
    LegalRequirementControl, ContactPerson, ResponsibleForFillingForm, ResponsibleForVerification,
    BiodeversidadeRecursosNaturais, Subproject, EnvironmentalSocialScreening,
    ConsultationAndEngagement, ScreeningResult, PreliminaryEnvironmentalInformation
)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EnvironmentalFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalFactor
        fields = '__all__'

class RisksAndImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RisksAndImpact
        fields = '__all__'

# class EnvironAndSocialRiskAndImapactAssessementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnvironAndSocialRiskAndImapactAssessement
#         fields = '__all__'

class EnvironAndSocialRiskAndImapactAssessementSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='departament.name', read_only=True)
    risks_impact_description = serializers.CharField(source='risks_and_impact.description', read_only=True)
    legal_requirement_titles = serializers.SerializerMethodField()
    environmental_factor_description = serializers.CharField(source='environmental_factor.description', read_only=True)

    class Meta:
        model = EnvironAndSocialRiskAndImapactAssessement
        fields = [
            'id',
            'intensity',
            'activity',
            'life_cycle',
            'statute',
            'probability',
            'significance',
            'description_of_measures',
            'deadline',
            'effectiveness_assessment',
            'compliance_requirements',
            'observations',
            'departament',
            'department_name', 
            'risks_and_impact',
            'risks_impact_description',
            'environmental_factor',
            'environmental_factor_description',
            'legal_requirements',
            'legal_requirement_titles',
            'observations',
            'created_by'
        ]
    def get_legal_requirement_titles(self, obj):
        # Fetch the document titles from the related LegalRequirement objects
        return [requirement.document_title for requirement in obj.legal_requirements.all()]

class LegalRequirementControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalRequirementControl
        fields = '__all__'

class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'

class ResponsibleForFillingFormSerializer(ContactPersonSerializer):
    class Meta:
        model = ResponsibleForFillingForm
        fields = '__all__'

class ResponsibleForVerificationSerializer(ContactPersonSerializer):
    class Meta:
        model = ResponsibleForVerification
        fields = '__all__'

class BiodeversidadeRecursosNaturaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiodeversidadeRecursosNaturais
        fields = '__all__'

class SubprojectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subproject
        fields = '__all__'

class EnvironmentalSocialScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalSocialScreening
        fields = '__all__'

class ConsultationAndEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationAndEngagement
        fields = '__all__'

class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = '__all__'

class PreliminaryEnvironmentalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreliminaryEnvironmentalInformation
        fields = '__all__'
