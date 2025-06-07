
import boto3

s3 = boto3.client('s3')

def list_s3_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']} - Created: {bucket['CreationDate']}")

list_s3_buckets()

