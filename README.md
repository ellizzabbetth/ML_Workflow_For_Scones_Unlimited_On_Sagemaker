# Udacity-Developing-Your-First-ML-Workflow
This is the Github repo for Udacity Developing your first ML workflow course. This repo contains the code for demos, exercises and the final project,
## Folder Structure
This repo contains a folder for each lesson and one project folder.

## Lessons Folder
Each lesson folder contains files for exercises and demos. The exercise code should contain instructions necessary for the exercises along with the solution. The demo code contains the files the instructor uses in the lesson demos.

## Project Folder
The project folder contains all files and instructions necessary for the project.


Meets Specifications
Dear Learner,
Good work, you have followed the correct steps to train, deploy the model and successfully completed the step function workflow
you have provided the required steps to perform the ETL process and uploaded the data to S3 bucket
Good work, you have created 3 lambda functions and deployed them. You have shared the lambda function script files as part of the submission
you have composed the Step function and successfully executed it
you have created an additional visualization based on the model monitor data
All the best
Further Reading 📚

Define a Pipeline
To orchestrate your workflows with Amazon SageMaker Model Building Pipelines, you need to generate a directed acyclic graph (DAG) in the form of a JSON pipeline definition.
Best practices for Step Functions
Train and Deploy a Machine Learning Model
Setup a SageMaker studio and a kernel to run this project

Good work, You have setup the workspace for the project execution.
Sagemaker provide various kernels and it is important to understand the requirement and use them efficiently with respect to operational requirement and cost

Further Reading 📚
Bring your own SageMaker image
You can create images and image versions, and attach image versions to your domain, using the SageMaker Studio control panel, the AWS SDK for Python (Boto3), and the AWS Command Line Interface (AWS CLI). You can also create images and image versions using the SageMaker console, even if you haven't onboarded to Studio.
💡 Tips for setting up a SageMaker Studio and a kernel:
Use a consistent naming convention for your notebooks and code. This will make it easier to find and manage your work.
Use version control to track your changes. This will help you keep track of your progress and make it easier to revert to previous versions of your work.
Document your work. This will help you remember what you did and why you did it. It will also be helpful for others who need to understand your work.
Students have completed the ETL (extract, transform, load) section of the starter code.

Well done, you have provided the required steps to perform the ETL process and uploaded the data to S3 bucket
However, you need to set stream=True for requests.get when downloading the data
This will help us to download large chunks of data without overlapping and it is best practice

Task
completed the ETL (extract, transform, load) section of the starter code. 🟢

Further Reading 📚
Define a Pipeline
To orchestrate your workflows with Amazon SageMaker Model Building Pipelines, you need to generate a directed acyclic graph (DAG) in the form of a JSON pipeline definition.
Students have successfully completed the Model training section up to “Getting ready to deploy”, showing they trained an image classification model

Perfect, you have trained the model by providing necessary hyper paramters, shows a good validation accuracy.
However, you can add more hyper paramters such as learning rate , batch size etc as part of experiments

Further Reading 📚

Real-time inference
Real-time inference is ideal for inference workloads where you have real-time, interactive, low latency requirements. You can deploy your model to SageMaker hosting services and get an endpoint that can be used for inference. These endpoints are fully managed and support autoscaling
Students have successfully completed the “Getting ready to deploy” section, showing they have deployed a trained ML model
Students have a unique model endpoint name printed in their notebook for use later in the project
Successfully made predictions using a sample image
Good work, you have deployed the model and used the Endpoint to derive inference based on the test data
completed the “Getting ready to deploy” section, showing they have deployed a trained ML model 🟢
unique model endpoint name printed in their notebook 🟢
made predictions using a sample image 🟢

Amazon SageMaker Model Building Pipelines
SageMaker Integration
SageMaker Pipelines is integrated directly with SageMaker, so you don't need to interact with any other AWS services. You also don't need to manage any resources because SageMaker Pipelines is a fully managed service, which means that it creates and manages resources for you.
💡 Best practices in model deployment in AWS SageMaker:
Use a production-ready model. Before you deploy a model to production, you should make sure that it is production-ready.

This means that the model has been thoroughly tested and that it meets all of the performance and accuracy requirements for your application.
Choose the right deployment method.

There are a variety of deployment methods available in SageMaker, each with its own advantages and disadvantages. The best deployment method for your application will depend on factors such as the type of model you are deploying, the volume of traffic you expect, and your budget.

Use a staging environment.
A staging environment is a separate environment where you can deploy your model before you deploy it to production. This allows you to test your model in a real-world environment and to make sure that it is working as expected before you expose it to production traffic.
Monitor your model performance.
Once you have deployed your model to production, you should monitor its performance. This will help you to identify any problems with the model and to make sure that it is meeting your performance requirements.
Use version control. Version control is a way to track changes to your code and data. This is important for model deployment because it allows you to roll back to a previous version of your model if there are any problems with the deployed model.
Build a full machine learning workflow
Students have authored three lambda functions.

1st lambda is responsible for return an object to step function as image_data in an event
2nd lambda is responsible for image classification
3rd lambada is responsible for filtering low-confidence inferences
Students have saved their code for each lambda function in a python script.

Good work, you have created 3 lambda functions and deployed them. You have shared the lambda function script files as part of the submission
Further Reading

Best practices for working with AWS Lambda functions
Use environment variables to pass operational parameters to your function. For example, if you are writing to an Amazon S3 bucket, instead of hard-coding the bucket name you are writing to, configure the bucket name as an environment variable.
Compose Lambdas together in a Step Function.
Students will have a JSON export that defines the Step Function
Students have a screenshot of the working Step Function.
Good work, you have composed the Step function and successfully executed it. Shared correct screenshot
Further reading
Best practices for Step Functions
Best practices for composing Lambdas together in a Step Function:
Use a consistent naming convention for your Lambda functions and Step Functions. This will make it easier to keep track of your code and troubleshoot any problems.

Use descriptive names for your states. This will make it easier to understand the flow of your Step Function.
Use the waitForTaskToken property when invoking a Lambda function from a Step Function. This will ensure that the Step Function waits for the Lambda function to finish executing before continuing.
Use error handling to gracefully handle errors in your Step Function. This will help to prevent your Step Function from failing.
Use the retry and catch clauses to handle errors in your Lambda functions. This will help to ensure that your Lambda functions are resilient to errors.
Use the timeout property to set a time limit for your Step Functions and Lambda functions. This will help to prevent your Step Functions and Lambda functions from running for too long
Monitor the model for errors
Students load the data from Model Monitor into their notebook

Correctly done, you have loaded the data from the data capture as part of model monitor into the notebook
Some best practices for using AWS Model Monitor:
Choose the right monitoring metrics. Model Monitor provides a variety of metrics to monitor, such as accuracy, precision, recall, and F1 score. Choose the metrics that are most important for your application.
Configure alerts. Model Monitor can send alerts when your model's performance degrades. Configure alerts so that you are notified as soon as possible of any problems.
Use explainability features. Model Monitor can provide explanations for your model's predictions. This can help you to understand why your model is making the predictions that it is.
Monitor your model in production. Once your model is in production, continue to monitor it. This will help you to ensure that your model is performing as expected.
Students create their own visualization of the Model Monitor data outputs

Well done, you have created an additional visualization based on the model monitor data, however you have reused the same visualization technique as before and made minor adjustment