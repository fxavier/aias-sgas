from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from riskmanagement.models import (
    Duration, Extension, LifeCycle, Intensity, Probability, ResponseType
)


from riskmanagement.models import (
    Department, EnvironmentalFactor, RisksAndImpact, EnvironAndSocialRiskAndImapactAssessement,
    LegalRequirementControl, ResponsibleForFillingForm, ResponsibleForVerification,
    BiodeversidadeRecursosNaturais, Subproject, EnvironmentalSocialScreening,
    ConsultationAndEngagement, ScreeningResult, PreliminaryEnvironmentalInformation
)
from riskmanagement.serializers import (
    DepartmentSerializer, EnvironmentalFactorSerializer, RisksAndImpactSerializer, 
    EnvironAndSocialRiskAndImapactAssessementSerializer, LegalRequirementControlSerializer, 
    ResponsibleForFillingFormSerializer, ResponsibleForVerificationSerializer, 
    BiodeversidadeRecursosNaturaisSerializer, SubprojectSerializer, 
    EnvironmentalSocialScreeningSerializer, ConsultationAndEngagementSerializer, 
    ScreeningResultSerializer, PreliminaryEnvironmentalInformationSerializer
)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EnvironmentalFactorViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalFactor.objects.all()
    serializer_class = EnvironmentalFactorSerializer

class RisksAndImpactViewSet(viewsets.ModelViewSet):
    queryset = RisksAndImpact.objects.all()
    serializer_class = RisksAndImpactSerializer

class EnvironAndSocialRiskAndImapactAssessementViewSet(viewsets.ModelViewSet):
    queryset = EnvironAndSocialRiskAndImapactAssessement.objects.all()
    serializer_class = EnvironAndSocialRiskAndImapactAssessementSerializer

class LegalRequirementControlViewSet(viewsets.ModelViewSet):
    queryset = LegalRequirementControl.objects.all()
    serializer_class = LegalRequirementControlSerializer

class ResponsibleForFillingFormViewSet(viewsets.ModelViewSet):
    queryset = ResponsibleForFillingForm.objects.all()
    serializer_class = ResponsibleForFillingFormSerializer

class ResponsibleForVerificationViewSet(viewsets.ModelViewSet):
    queryset = ResponsibleForVerification.objects.all()
    serializer_class = ResponsibleForVerificationSerializer

class BiodeversidadeRecursosNaturaisViewSet(viewsets.ModelViewSet):
    queryset = BiodeversidadeRecursosNaturais.objects.all()
    serializer_class = BiodeversidadeRecursosNaturaisSerializer

class SubprojectViewSet(viewsets.ModelViewSet):
    queryset = Subproject.objects.all()
    serializer_class = SubprojectSerializer

class EnvironmentalSocialScreeningViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalSocialScreening.objects.all()
    serializer_class = EnvironmentalSocialScreeningSerializer

class ConsultationAndEngagementViewSet(viewsets.ModelViewSet):
    queryset = ConsultationAndEngagement.objects.all()
    serializer_class = ConsultationAndEngagementSerializer

class ScreeningResultViewSet(viewsets.ModelViewSet):
    queryset = ScreeningResult.objects.all()
    serializer_class = ScreeningResultSerializer

class PreliminaryEnvironmentalInformationViewSet(viewsets.ModelViewSet):
    queryset = PreliminaryEnvironmentalInformation.objects.all()
    serializer_class = PreliminaryEnvironmentalInformationSerializer

class DurationViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in Duration.choices}
        return Response(choices)

class ExtensionViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in Extension.choices}
        return Response(choices)
    
class LifeCycleViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in LifeCycle.choices}
        return Response(choices)
    
class IntensityViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in Intensity.choices}
        return Response(choices)
    
class ProbabilityViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in Probability.choices}
        return Response(choices)
    
class ResponseTypeViewSet(ViewSet):
    def list(self, request):
        choices = {choice[0]: choice[1] for choice in ResponseType.choices}
        return Response(choices)
    

    
