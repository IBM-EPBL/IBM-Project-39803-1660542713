import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "nWuZ-MwC66AvzoGmTx_XcdipJXLDl6lfTAOxk585LMT2" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:iam-identity::a/0f4afbcee52444c89d7471691606e761::serviceid:ServiceId-bb6de0e8-f19e-46d0-bab5-559d265d9fa7",
def get_bucket_contents(newswaves2):
    print("Retrieving bucket contents from: {0}".format(newswaves2))
    try:
        files = cos.Bucket(newswaves2).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))