import logging
import boto3
from botocore.exceptions import ClientError


def copy_object(
    src_bucket_name, 
    src_object_name,
    dest_bucket_name, 
    dest_object_name=None
    ):
        
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    if dest_object_name is None:
        dest_object_name = src_object_name
        
    s3 = boto3.client('s3')
    try:
        s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                       Key=dest_object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    src_bucket_name = 'yanjunchen-123456'
    src_object_name = 'my_1st_object'
    dest_bucket_name = 'the2th'
    dest_object_name = '1st_ob_copy'

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    success = copy_object(src_bucket_name, src_object_name,
                         dest_bucket_name, dest_object_name)
    if success:
        logging.info(f'Copied {src_bucket_name}/{src_object_name} to '
                     f'{dest_bucket_name}/{dest_object_name}')


if __name__ == '__main__':
    main()
