import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(name):
    try:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket = name)
    except ClientError:
        logging.error(ClientError)  
        return False
    return True

busket_name = input("Name of the new busket: ")
create_bucket(busket_name)