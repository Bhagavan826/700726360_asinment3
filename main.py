import boto3
import configparser

sqs = boto3.client('sqs')


queue_name = 'queue'
queue_attributes = {
    'DelaySeconds': '0',
    'VisibilityTimeout': '30'
}

response = sqs.create_queue(
    QueueName=queue_name,
    Attributes=queue_attributes
)
print(f'Queue created: {response["QueueUrl"]}')