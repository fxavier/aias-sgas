import boto3
from botocore.exceptions import ClientError
from django.http import HttpResponse, Http404
from django.conf import settings
import mimetypes

def download_file(request, file_key):
    """
    View to download a file from Supabase storage
    """
    # Initialize S3 client with Supabase credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        region_name=settings.AWS_S3_REGION_NAME
    )
    
    try:
        # Get the file from Supabase storage
        file_obj = s3_client.get_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=file_key
        )
        
        # Determine content type
        content_type = file_obj.get('ContentType')
        if not content_type:
            content_type = mimetypes.guess_type(file_key)[0] or 'application/octet-stream'
        
        # Set the filename from the key for the download
        filename = file_key.split('/')[-1]
        
        # Create the response with the file
        response = HttpResponse(file_obj['Body'].read(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise Http404("File not found")
        else:
            # Log the error and return a 500 response
            print(f"Error downloading file: {e}")
            return HttpResponse(status=500) 