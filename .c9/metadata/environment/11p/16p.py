{"filter":false,"title":"16p.py","tooltip":"/11p/16p.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["import boto3","import botocore","","BUCKET_NAME = 'my-bucket' # replace with your bucket name","KEY = 'my_image_in_s3.jpg' # replace with your object key","","s3 = boto3.resource('s3')","","try:","    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')","except botocore.exceptions.ClientError as e:","    if e.response['Error']['Code'] == \"404\":","        print(\"The object does not exist.\")","    else:","        raise"," "],"id":1}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":57},"action":"remove","lines":[" # replace with your bucket name"],"id":2}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":57},"action":"remove","lines":[" # replace with your object key"],"id":3}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":24},"action":"remove","lines":["bucket"],"id":4},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["-"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["y"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["m"]}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"],"id":5},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["h"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["e"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["2"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["t"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["h"]}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":25},"action":"remove","lines":["my_image_in_s3.jpg"],"id":6},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["1"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["s"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["t"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["o"],"id":7},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["b"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["_"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["c"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["p"],"id":8},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":47},"end":{"row":9,"column":65},"action":"remove","lines":["my_local_image.jpg"],"id":9},{"start":{"row":9,"column":47},"end":{"row":9,"column":58},"action":"insert","lines":["1st_ob_copy"]}],[{"start":{"row":9,"column":47},"end":{"row":9,"column":58},"action":"remove","lines":["1st_ob_copy"],"id":10},{"start":{"row":9,"column":47},"end":{"row":9,"column":83},"action":"insert","lines":["/home/ec2-user/environment/11p/a.txt"]}],[{"start":{"row":9,"column":78},"end":{"row":9,"column":83},"action":"remove","lines":["a.txt"],"id":11},{"start":{"row":9,"column":78},"end":{"row":9,"column":79},"action":"insert","lines":["d"]},{"start":{"row":9,"column":79},"end":{"row":9,"column":80},"action":"insert","lines":["o"]},{"start":{"row":9,"column":80},"end":{"row":9,"column":81},"action":"insert","lines":["w"]},{"start":{"row":9,"column":81},"end":{"row":9,"column":82},"action":"insert","lines":["n"]},{"start":{"row":9,"column":82},"end":{"row":9,"column":83},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":83},"end":{"row":9,"column":84},"action":"insert","lines":["o"],"id":12},{"start":{"row":9,"column":84},"end":{"row":9,"column":85},"action":"insert","lines":["a"]},{"start":{"row":9,"column":85},"end":{"row":9,"column":86},"action":"insert","lines":["d"]}],[{"start":{"row":9,"column":86},"end":{"row":9,"column":87},"action":"insert","lines":["."],"id":13},{"start":{"row":9,"column":87},"end":{"row":9,"column":88},"action":"insert","lines":["t"]},{"start":{"row":9,"column":88},"end":{"row":9,"column":89},"action":"insert","lines":["x"]},{"start":{"row":9,"column":89},"end":{"row":9,"column":90},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":1},"end":{"row":15,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1580043458242,"hash":"d478e2a9cd4ffc4a5acea6a194a286f6447d5d03"}