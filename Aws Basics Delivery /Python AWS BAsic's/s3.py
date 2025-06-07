
import boto3

s3 = boto3.client('s3')
bucket_name = 'coderrange-s3-demo-bucket-venkatesh'

file_path = 'venkat.txt'

# Create a small file
with open(file_path, 'w') as f:
    f.write("Hello from Python and AWS S3!")

# Upload to S3
s3.upload_file(file_path, bucket_name, 'venkat.txt')
print("✅ File uploaded to S3")
