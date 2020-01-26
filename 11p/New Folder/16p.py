import boto3
import botocore

BUCKET_NAME = 'the2th'
KEY = '1st_ob_copy'

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, '/home/ec2-user/environment/11p/download.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
 