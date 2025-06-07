
import boto3

def list_s3_buckets():
    s3 = boto3.client('s3', region_name='us-east-1')
    response = s3.list_buckets()
    print("Buckets:", [bucket['Name'] for bucket in response['Buckets']])

list_s3_buckets()
