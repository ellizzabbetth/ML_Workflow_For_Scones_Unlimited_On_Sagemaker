

create Lambda execution role since by default, sagemaker execution roles won't have access to Lambda:
https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3-lambda-permissions.html#sms-custom-templates-step3-postlambda-execution-role-perms

So I added the following customer inline policy to AmazonSageMaker-ExecutionRole-20240131T143273:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "arn:aws:lambda:us-east-1:755707037007:function:filterInterference",
                "arn:aws:lambda:us-east-1:755707037007:function:filterInterference:*",
                "arn:aws:lambda:us-east-1:755707037007:function:inferImage",
                "arn:aws:lambda:us-east-1:755707037007:function:inferImage:*"
            ]
        }
    ]
}

First Lambda Function Input:
Your input JSON should be the one you generated from the notebook. Please search with "generate_test_case" and find the code for the test case generation.

For example: '{"image_data": "", "s3_bucket": "sagemaker-us-east-1-755707037007", "s3_key": "test/motorcycle_s_001906.png"}'