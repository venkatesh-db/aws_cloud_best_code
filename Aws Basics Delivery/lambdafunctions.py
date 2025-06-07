
import boto3

lambda_client = boto3.client('lambda')
role_arn = 'arn:aws:iam::293595299410:role/your-lambda-execution-role'

def create_lambda():
    with open('lambda_function.zip', 'rb') as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName='MyLambdaFunction',
        Runtime='python3.10',
        Role=role_arn,
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': zipped_code},
        Timeout=15,
        Publish=True
    )
    print("Lambda function created:", response['FunctionArn'])

create_lambda()
