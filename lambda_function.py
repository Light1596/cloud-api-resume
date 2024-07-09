import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    
    
    table = dynamodb.Table('Resumes')
    
    # Log the received event for debugging purposes
    print("Received event:", json.dumps(event))
    
    # Extract the email from query string parameters 
    query_params = event.get('queryStringParameters')
    
    if not query_params:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'queryStringParameters are required'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    email = query_params.get('Email')
    
    if not email:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Email query parameter is required'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    try:
        # Query the table for the item with the specified email
        response = table.query(
            KeyConditionExpression=Key('Email').eq(email)
        )
        
        # Check if an item was found
        if 'Items' in response and response['Items']:
            item = response['Items'][0]
            
            # Convert sets to lists. This is because sets are not serializable
            def convert_sets(obj):
                if isinstance(obj, set):
                    return list(obj)
                elif isinstance(obj, dict):
                    return {k: convert_sets(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_sets(i) for i in obj]
                else:
                    return obj
            
            # Calling the function
            item = convert_sets(item)
            
            return {
                'statusCode': 200,
                'body': json.dumps(item),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'  # To handle CORS if needed
                }
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'}),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
