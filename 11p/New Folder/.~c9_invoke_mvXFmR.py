import logging
import boto3
from botocore.exceptions import ClientError


def get_object_acl(bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object_acl(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return None

def main():
    """Exercise get_object_acl()"""

    # Assign these values before running the program
    test_bucket_name = 'BUCKET_NAME'
    test_object_name = 'OBJECT_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the object's current access control list
    acl = get_object_acl(test_bucket_name, test_object_name)
    if acl is None:
        exit(-1)

    # Output the object ACL grantees and permissions
    for grantee in acl['Grants']:
        # The grantee type determines the grantee_identifier
        grantee_type = grantee['Grantee']['Type']
        if grantee_type == 'CanonicalUser':
            grantee_identifier = grantee['Grantee']['DisplayName']
        elif grantee_type == 'AmazonCustomerByEmail':
            grantee_identifier = grantee['Grantee']['EmailAddress']
        elif grantee_type == 'Group':
            grantee_identifier = grantee['Grantee']['URI']
        else:
            grantee_identifier = 'Unknown'
        logging.info(f'Grantee: {grantee_identifier}, '
                     f'Permissions: {grantee["Permission"]}')


if __name__ == '__main__':
    main()
