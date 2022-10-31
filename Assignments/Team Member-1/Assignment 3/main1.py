import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "1VAFTqWATTPwYWGbNnBMQ1vQEKx7zVaLFU5piTzxNQem" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:iam-identity::a/c2b87f32fe6d49529d17642036209763::serviceid:ServiceId-e7204bb6-e6bb-4170-8709-7512e1d0c531"
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