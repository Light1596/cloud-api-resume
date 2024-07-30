import json
import boto3

def lambda_handler(event, context):
    dynamodb_client = boto3.resource('dynamodb')
    dynamodb_table = dynamodb_client.Table('Resumes')
    
    try:
        # Fetch the item by its primary key
        response = dynamodb_table.get_item(Key={'id': '1'})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
        
        item = response['Item']
        
        return {
            'statusCode': 200,
            'body': json.dumps(item, cls=CustomEncoder)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
