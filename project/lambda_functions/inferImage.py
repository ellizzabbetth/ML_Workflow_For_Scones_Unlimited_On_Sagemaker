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