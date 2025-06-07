
import boto3

s3 = boto3.client('s3')
bucket_name = 'coderrange-s3-demo-bucket-venkatesh'
file_path = 'secure-data.txt'

# Create a test file
with open(file_path, 'w') as f:
    f.write("Sensitive data")

# Upload with encryption
s3.upload_file(
    file_path,
    bucket_name,
    'secure-data.txt',
    ExtraArgs={
        'ServerSideEncryption': 'AES256'  # or 'aws:kms' for KMS encryption
    }
)

print("🔐 Secure upload with server-side encryption complete")
