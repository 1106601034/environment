import logging
import boto3
from botocore.exceptions import ClientError


def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    test_bucket_name = 'yanjunchen-123456'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    if delete_bucket(test_bucket_name):
        logging.info(f'{test_bucket_name} was deleted')


if __name__ == '__main__':
    main()
