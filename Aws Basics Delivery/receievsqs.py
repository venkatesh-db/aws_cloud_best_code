
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/293595299410/my-queue'

def receive_messages():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=5
    )
    messages = response.get('Messages', [])
    for msg in messages:
        print(f"Received: {msg['Body']}")

receive_messages()
