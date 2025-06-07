
import boto3
import json

lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName='your-lambda-function-name',
    InvocationType='RequestResponse',
    Payload=json.dumps({"key": "value"}),
)

print("🤖 Lambda Output:", response['Payload'].read().decode("utf-8"))
