import boto3
from app.core.config import settings

# DynamoDB resource
dynamodb = boto3.resource(
    "dynamodb",
    region_name=settings.AWS_REGION
)

# Main table used by the application
table = dynamodb.Table(settings.TABLE_NAME)

# SQS client (if used for async messaging)
sqs = boto3.client(
    "sqs",
    region_name=settings.AWS_REGION
)

# EventBridge client (for events / scheduling / triggers)
events = boto3.client(
    "events",
    region_name=settings.AWS_REGION
)