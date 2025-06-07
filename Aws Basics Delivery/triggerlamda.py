
import boto3

lambda_client = boto3.client('lambda')

def invoke_lambda():
    response = lambda_client.invoke(
        FunctionName='MyLambdaFunction',
        InvocationType='RequestResponse',
        Payload=b'{}'
    )
    print(response['Payload'].read().decode())

invoke_lambda()
