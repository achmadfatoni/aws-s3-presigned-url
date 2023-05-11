import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta

print('Generate presign url...')

# Replace with your S3 bucket name and object key
BUCKET_NAME = 'bucket-name-here'
OBJECT_KEY = 'file-name-here'

# Create a Boto3 S3 client
s3_client = boto3.client('s3')

# Generate a pre-signed URL for the S3 object that will expire in 1 hour
expiration = datetime.now() + timedelta(hours=1)
try:
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': BUCKET_NAME,
            'Key': OBJECT_KEY
        },
        ExpiresIn=3600,
    )
    print(f'Url will be expired at {expiration}')
    print(f'Pre-signed URL: {presigned_url}')
except ClientError as e:
    print(f'Error generating pre-signed URL: {e}')