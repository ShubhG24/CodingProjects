import json
import boto3

REGION = "us-east-1"
s3 = boto3.resource('s3',region_name=REGION)
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')


def lambda_handler(event, context):
  #  return {"data":event}
    photoID = event['body-json']['photoID']  # assuming the client sends the PhotoID of the image to be deleted
    
    table.delete_item(
            Key={
                'PhotoID': str(photoID), 'CreationTime':int(photoID)
            }
        )
        
    return {
            "statusCode": 200,
            "body": json.dumps("Photo deleted successfully.")
        }
    #try:
        # response = table.get_item(
        #     Key={
        #         'PhotoID': photoID,
        #           'CreationTime':int(photoID)
        #     }
        # )
         
        # item = response.get('Item')
       
    #     if not item:
    #         return {
    #             "statusCode": 404,
    #             "body": json.dumps("Photo not found.")
    #         }
        
    #     # Extract the S3 object key from the URL
    #     object_key = item['URL'].split('/')[-1]
    #   # return {"data":object_key}
    #     # Delete the object from S3
    #     bucket_name="photobucket-gundepudi-2024-4150"
    #     s3 = boto3.resource('s3')
    #     bucket = s3.Bucket(bucket_name)
    #     bucket.delete_item(object_key)
    #     return {"s":object_key}

        # Delete the item from DynamoDB

        
    # except Exception as e:
    #     print(e)
    #     return {
    #         "statusCode": 500,
    #         "body": json.dumps("An error occurred."),
    #         "error":e,
    #         "item":photoID,
    #         "event":event
            
    #     }