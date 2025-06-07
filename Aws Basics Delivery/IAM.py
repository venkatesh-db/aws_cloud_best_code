
import boto3

iam = boto3.client('iam')

def list_iam_users():
    response = iam.list_users()
    print(response)
    for user in response['Users']:
        print(f"User: {user['UserName']} - Created: {user['CreateDate']}")

list_iam_users()
