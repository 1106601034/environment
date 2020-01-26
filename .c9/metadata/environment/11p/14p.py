{"filter":false,"title":"14p.py","tooltip":"/11p/14p.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":65,"column":0},"action":"insert","lines":["# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]","# snippet-sourcedescription:[delete_bucket.py demonstrates how to delete an empty Amazon S3 bucket.]","# snippet-service:[s3]","# snippet-keyword:[Amazon S3]","# snippet-keyword:[Python]","# snippet-sourcesyntax:[python]","# snippet-sourcesyntax:[python]","# snippet-keyword:[Code Sample]","# snippet-sourcetype:[full-example]","# snippet-sourcedate:[2019-2-12]","# snippet-sourceauthor:[AWS]","","# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.","#","# This file is licensed under the Apache License, Version 2.0 (the \"License\").","# You may not use this file except in compliance with the License. A copy of the","# License is located at","#","# http://aws.amazon.com/apache2.0/","#","# This file is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS","# OF ANY KIND, either express or implied. See the License for the specific","# language governing permissions and limitations under the License.","","import logging","import boto3","from botocore.exceptions import ClientError","","","def delete_bucket(bucket_name):","    \"\"\"Delete an empty S3 bucket","","    If the bucket is not empty, the operation fails.","","    :param bucket_name: string","    :return: True if the referenced bucket was deleted, otherwise False","    \"\"\"","","    # Delete the bucket","    s3 = boto3.client('s3')","    try:","        s3.delete_bucket(Bucket=bucket_name)","    except ClientError as e:","        logging.error(e)","        return False","    return True","","","def main():","    \"\"\"Exercise delete_bucket()\"\"\"","","    # Assign this value before running the program","    test_bucket_name = 'BUCKET_NAME'","","    # Set up logging","    logging.basicConfig(level=logging.DEBUG,","                        format='%(levelname)s: %(asctime)s: %(message)s')","","    # Delete the bucket","    if delete_bucket(test_bucket_name):","        logging.info(f'{test_bucket_name} was deleted')","","","if __name__ == '__main__':","    main()",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]","# snippet-sourcedescription:[delete_bucket.py demonstrates how to delete an empty Amazon S3 bucket.]","# snippet-service:[s3]","# snippet-keyword:[Amazon S3]","# snippet-keyword:[Python]","# snippet-sourcesyntax:[python]","# snippet-sourcesyntax:[python]","# snippet-keyword:[Code Sample]","# snippet-sourcetype:[full-example]","# snippet-sourcedate:[2019-2-12]","# snippet-sourceauthor:[AWS]","","# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.","#","# This file is licensed under the Apache License, Version 2.0 (the \"License\").","# You may not use this file except in compliance with the License. A copy of the","# License is located at","#","# http://aws.amazon.com/apache2.0/","#","# This file is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS","# OF ANY KIND, either express or implied. See the License for the specific","# language governing permissions and limitations under the License.","",""],"id":2}],[{"start":{"row":5,"column":31},"end":{"row":14,"column":23},"action":"remove","lines":["","    \"\"\"Delete an empty S3 bucket","","    If the bucket is not empty, the operation fails.","","    :param bucket_name: string","    :return: True if the referenced bucket was deleted, otherwise False","    \"\"\"","","    # Delete the bucket"],"id":3}],[{"start":{"row":15,"column":11},"end":{"row":18,"column":50},"action":"remove","lines":["","    \"\"\"Exercise delete_bucket()\"\"\"","","    # Assign this value before running the program"],"id":4}],[{"start":{"row":16,"column":36},"end":{"row":18,"column":20},"action":"remove","lines":["","","    # Set up logging"],"id":5}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":23},"action":"remove","lines":["    # Delete the bucket"],"id":6},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":24},"end":{"row":16,"column":35},"action":"remove","lines":["BUCKET_NAME"],"id":7},{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"insert","lines":["y"]},{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"insert","lines":["a"]},{"start":{"row":16,"column":26},"end":{"row":16,"column":27},"action":"insert","lines":["n"]},{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"insert","lines":["j"]},{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"insert","lines":["u"]},{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"insert","lines":["n"]},{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"insert","lines":["c"]},{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"insert","lines":["h"]},{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["e"]},{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["-"],"id":8},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["1"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["2"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["3"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["4"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["5"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["6"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":55},"end":{"row":21,"column":55},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1580042623838,"hash":"0e02aaea8f8bfec14f88c5236f67832e3a431e8e"}