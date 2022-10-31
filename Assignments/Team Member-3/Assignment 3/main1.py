import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "7f2rzKOCyo0AhYmce1o9NN1RuFFEyGIBBaiTdqX1r1rG" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:iam-identity::a/c2b87f32fe6d49529d17642036209763::serviceid:ServiceId-29fed175-65a4-40bb-a76c-d5b8d817627f" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696

def get_bucket_contents(newswaves3):
    print("Retrieving bucket contents from: {0}".format(newswaves3))
    try:
        files = cos.Bucket(newswaves3).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))