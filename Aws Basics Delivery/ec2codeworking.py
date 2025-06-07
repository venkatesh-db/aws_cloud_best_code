
import boto3

# Create EC2 client
#ec2 = boto3.resource('ec2')
ec2 = boto3.resource('ec2', region_name='us-east-1')


# Launch EC2 instance

instance = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (us-east-1 example)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',          # Free-tier eligible
    KeyName='venkatesh',            # Replace with your key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyFirstInstance'}]
        }
    ]
)

print("Launched EC2 Instance with ID:", instance[0].id)
