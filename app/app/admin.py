from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from core.admin import *

class CustomAdminSite(admin.AdminSite):
    site_header = 'SGAS - Sistema de gestão ambiental e social'
    site_title = 'SGAS'
    index_title = 'SGAS'

    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        app_names = {
            "riskmanagement": "IDENTIFICATION OF RISKS AND IMPACTS",
            "programsmanagement": "PROGRAMS MANAGEMENT",
            "organizationalcapacityandcompetency": "ORGANIZATIONAL CAPACITY AND COMPETENCY",
            "emergencyresponse": "EMERGENCY PREPAREDNESS AND RESPONSE",
            "extcommungrievancemechanism": "EXTERNAL COMMUNICATIONS AND GRIEVANCE MECHANISMS",
            "reportingmonitoringandreview": "MONITORING AND REVIEW",
            "documentmanagement": "DOCUMENT MANAGEMENT",
            "resourceefficiencyandpollutionprevention": "RESOURCE EFFICIENCY AND POLLUTION PREVENTION",
            
        }
        

        # Apply the custom app names
        for app in app_list:
            app_label = app['app_label']
            if app_label in app_names:
                app['name'] = app_names[app_label]


        app_ordering = {
            "riskmanagement": 1,
            "programsmanagement": 2,
            "organizationalcapacityandcompetency": 3,
            "emergencyresponse": 4,
            "extcommungrievancemechanism": 5,
            "reportingmonitoringandreview": 6,
            "documentmanagement": 7,
            "resourceefficiencyandpollutionprevention": 8,
            "auth": 9,
        
        }

        # Sort apps
        app_list.sort(key=lambda app: app_ordering.get(app['app_label'], 999))
       

        # Sort models within apps
        
        model_ordering = {
           "riskmanagement": {
                "EnvironAndSocialRiskAndImapactAssessement": 1,
                "LegalRequirementControl": 2,
                "EnvironmentalSocialScreening": 3,
                "PreliminaryEnvironmentalInformation": 4,
                "LegalRequirementControl": 5,
                "ContactPerson": 6,
                "Subproject": 7,
                "ConsultationAndEngagement": 8,
                "RiskRevScreeningResultiew": 9,
                "EmbeddedMitigation": 10,
                "PlanningOrConstructionPhase": 11,
           },
           "organizationalcapacityandcompetency": {
                "TrainingNeeds": 1,
                "TrainingPlan": 2,
                "TrainingMatrix": 3,
                "TrainingEffectivnessAssessment": 4,
                "OHSACTING": 5,
                "ToolBoxTalks": 6,
                "Training": 7,
                "TrainingEvaluationQuestions": 8,
                "AcceptanceConfirmation": 9,
            
           },

            "emergencyresponse": {
                "RelatorioAcidenteIncidente": 1,
                "ListaVerificacaoKitPrimeirosSocorros": 2,
                "IncidentFlashReport": 3,
                "PessoaEnvolvida": 4,
                "ListaVerificacaoKitPrimeirosSocorros": 5,
                "IncidentFlashReport": 6,
                "PessoaEnvolvida": 7,
                "PessoasEnvolvidasNaInvestigacao": 8,
                "AccoesImediatasECorrectivas": 9,
                
            },

            "extcommungrievancemechanism": {
                "ClaimComplainControl": 1,
                "ClaimNonComplianceControl": 2,
                "ComplaintAndClaimRecord": 3,
                "WorkerGrievance": 4,
                "WorkerGrievanceRecord": 5,
                "PhotoDocumentProvingClosure": 6,
            },

        }

        # Sort models within each app
        for app in app_list:
            app_label = app['app_label']
            if app_label in model_ordering:
                app['models'].sort(
                    key=lambda model: model_ordering[app_label].get(model['object_name'], 999)
                )

            
       
        return app_list
        

        

custom_admin_site = CustomAdminSite(name='sgas_admin')

#custom_admin_site.register(User, UserAdmin)
#custom_admin_site.register(Group, GroupAdmin)


     
                