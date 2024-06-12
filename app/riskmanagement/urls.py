from rest_framework import routers
from django.urls import path, include
from riskmanagement.views import (
    DepartmentViewSet, EnvironmentalFactorViewSet, RisksAndImpactViewSet, 
    EnvironAndSocialRiskAndImapactAssessementViewSet, LegalRequirementControlViewSet, 
    ResponsibleForFillingFormViewSet, ResponsibleForVerificationViewSet, 
    BiodeversidadeRecursosNaturaisViewSet, SubprojectViewSet, 
    EnvironmentalSocialScreeningViewSet, ConsultationAndEngagementViewSet, 
    ScreeningResultViewSet, PreliminaryEnvironmentalInformationViewSet
)

router = routers.DefaultRouter()

router.register('departments', DepartmentViewSet)
router.register('environmental-factors', EnvironmentalFactorViewSet)
router.register('risks-and-impacts', RisksAndImpactViewSet)
router.register('environ-and-social-risk-and-impact-assessments', EnvironAndSocialRiskAndImapactAssessementViewSet)
router.register('legal-requirement-controls', LegalRequirementControlViewSet)
router.register('responsible-for-filling-forms', ResponsibleForFillingFormViewSet)
router.register('responsible-for-verifications', ResponsibleForVerificationViewSet)
router.register('biodiversidade-recursos-naturais', BiodeversidadeRecursosNaturaisViewSet)
router.register('subprojects', SubprojectViewSet)
router.register('environmental-social-screenings', EnvironmentalSocialScreeningViewSet)
router.register('consultation-and-engagements', ConsultationAndEngagementViewSet)
router.register('screening-results', ScreeningResultViewSet)
router.register('preliminary-environmental-information', PreliminaryEnvironmentalInformationViewSet)

app_name = 'riskmanagement'

urlpatterns = [
    path('', include(router.urls)),
]
