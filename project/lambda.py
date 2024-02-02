import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event["s3_key"]
    bucket = event["s3_bucket"]

    # Download the data from s3 to /tmp/image.png
    try:
        s3.download_file(bucket, key, '/tmp/image.png')
    except:
        raise
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

import json
import os
import io
import boto3
import base64
# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2024-02-01-11-52-30-952' ## TODO: fill in
runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Make a prediction
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,ContentType='image/png',Body=image)
    inferences = response['Body'].read().decode('utf-8')
    event["inferences"] = [float(x) for x in inferences[1:-1].split(',')]

    # Return the inferences
    return {
        'statusCode': 200,
        'body': {
            'image_data': event['image_data'],
            's3_bucket': event['s3_bucket'],
            's3_key': event['s3_key'],
            'inferences': event['inferences']
        }
        
    }

import json


THRESHOLD = .75


def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event['inferences']

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(i > THRESHOLD for i in inferences)

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': {
            'image_data': event['image_data'],
            's3_bucket': event['s3_bucket'],
            's3_key': event['s3_key'],
            'inferences': event['inferences']
        }
    }