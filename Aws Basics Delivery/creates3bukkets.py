
import boto3

def create_bucket(bucket_name):
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket=bucket_name)  # No LocationConstraint needed
    print("created sucessfully")

create_bucket('coderrange-s3-demo-bucket-venkatesh')
