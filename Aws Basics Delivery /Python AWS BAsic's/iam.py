
import boto3

reply=boto3.client('iam')
resp=reply.list_users()
print(resp)

for i in resp['Users']:
    print("i am hero",i['UserName'])

