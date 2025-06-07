
import boto3

s3 = boto3.client('s3')

def upload_file(bucket_name, file_path, key):
    s3.upload_file(file_path, bucket_name, key)
    print(f"Uploaded {file_path} as {key} to {bucket_name}")

upload_file('coderrange-s3-demo-bucket-venkatesh', 'localfile.txt', 'uploadedfile.txt')
