
import boto3

ec2 = boto3.client('ec2')

def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Started EC2 instance: {instance_id}")

def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopped EC2 instance: {instance_id}")

# Example usage
# start_instance('i-0abcdef1234567890')
# stop_instance('i-0abcdef1234567890')
