
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/293595299410/my-queue'

def send_message():
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Hello Coderrange from boto3!'
    )
    print(f"Message sent! ID: {response['MessageId']}")

send_message()
