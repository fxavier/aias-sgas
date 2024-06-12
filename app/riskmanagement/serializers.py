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

class EnvironAndSocialRiskAndImapactAssessementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironAndSocialRiskAndImapactAssessement
        fields = '__all__'

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
