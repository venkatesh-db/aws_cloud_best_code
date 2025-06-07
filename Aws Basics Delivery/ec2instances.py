
import boto3

ec2 = boto3.client('ec2')

def list_ec2_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
    print("ec2 runing smoothly")

list_ec2_instances()
