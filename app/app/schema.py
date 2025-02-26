import graphene
from documentmanagement.schema import Query as DocumentQuery, Mutation as DocumentMutation
from emergencyresponse.schema import Query as EmergencyResponseQuery, Mutation as EmergencyResponseMutation
from extcommungrievancemechanism.schema import Query as ExtcommungrievancemechanismQuery, Mutation as ExtcommungrievancemechanismMutation
from organizationalcapacityandcompetency.schema import(
            Query as OrganizationalcapacityandcompetencyQuery, 
            Mutation as OrganizationalcapacityandcompetencyMutation
)
from programsmanagement.schema import Query as ProgramsmanagementQuery, Mutation as ProgramsmanagementMutation
from reportingmonitoringandreview.schema import (
           Query as ReportingmonitoringandreviewQuery, Mutation as ReportingmonitoringandreviewMutation
)
from resourceefficiencyandpollutionprevention.schema import (
            Query as ResourceefficiencyandpollutionpreventionQuery, 
            Mutation as ResourceefficiencyandpollutionpreventionMutation
)
from riskmanagement.schema import (
            Query as RiskmanagementQuery, 
            Mutation as RiskmanagementMutation
)
from users.schema import Query as UserQuery, Mutation as UserMutation
from graphene import String
import boto3
from django.conf import settings
from graphene import ObjectType


class Query(DocumentQuery, EmergencyResponseQuery, ExtcommungrievancemechanismQuery, 
            OrganizationalcapacityandcompetencyQuery, ProgramsmanagementQuery, 
            ReportingmonitoringandreviewQuery, ResourceefficiencyandpollutionpreventionQuery, 
            RiskmanagementQuery, UserQuery, graphene.ObjectType):
    # New query to get a download URL
    get_file_download_url = String(file_key=String(required=True))
    
    def resolve_get_file_download_url(self, info, file_key):
        """Generate a pre-signed URL for file download"""
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            region_name=settings.AWS_S3_REGION_NAME
        )
        
        try:
            # Generate a pre-signed URL for the file (valid for 1 hour)
            url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Key': file_key
                },
                ExpiresIn=3600  # URL expires in 1 hour
            )
            return url
        except Exception as e:
            print(f"Error generating presigned URL: {e}")
            return None

class Mutation(DocumentMutation, EmergencyResponseMutation, ExtcommungrievancemechanismMutation,
                OrganizationalcapacityandcompetencyMutation, ProgramsmanagementMutation, 
                ReportingmonitoringandreviewMutation, ResourceefficiencyandpollutionpreventionMutation, 
                RiskmanagementMutation, UserMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)