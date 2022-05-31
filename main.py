#import statements go here
import requests
import json

# NAME OF THE FUNCTION IN AWS LAMBDA; by default, the name is "lambda_handler" or "my_handler" in the documentation
# this must be the name of your function as defined in AWS Lambda. 
# This will be the function that AWS Lambda calls.
def lambda_handler(event, context):
    #IMPORTANT: json format for making the results accessible through the API Gateway
    response = {
        "statusCode": 200,
        "body": {
            "message": "Welcome to AWS lambda!",
        }
    }
    return response
