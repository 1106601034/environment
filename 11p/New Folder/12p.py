import logging
import boto3
from botocore.exceptions import ClientError


def put_object(dest_bucket_name, dest_object_name, src_data):
    if isinstance(src_data, bytes):
        object_data = src_data
    elif isinstance(src_data, str):
        try:
            object_data = open(src_data, 'rb')
        except Exception as e:
            logging.error(e)
            return False
    else:
        logging.error('Type of ' + str(type(src_data)) +
                      ' for the argument \'src_data\' is not supported.')
        return False

    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=dest_bucket_name, Key=dest_object_name, Body=object_data)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        if isinstance(src_data, str):
            object_data.close()
    return True

test_bucket_name = 'yanjunchen-123456'
test_object_name = 'my_1st_object'
filename = '/home/ec2-user/en1p/a.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s: %(message)s')
success = put_object(test_bucket_name, test_object_name, filename)
if success:
    logging.info(f'Added {test_object_name} to {test_bucket_name}')
