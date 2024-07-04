# ABOUT
When the HTTP API is invoked, the API gateway routes the request to the Lambda function.
The Lambda function interacts with DynamoDB, and returns a response to the API Gateway. 
The API gtaeway then returns the resume response to the end user.
