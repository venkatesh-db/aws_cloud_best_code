
import boto3

# No keys here; boto3 will use the IAM role attached to the instance or Lambda
s3 = boto3.client('s3')

response = s3.list_buckets()

for i in response['Buckets']:
    print(i['Name'])

print("🛡️ Secure access – Buckets:", [bucket['Name'] for bucket in response['Buckets']])
