import boto3

client_table = boto3.client('dynamodb')

response = client_table.get_item(TableName='Resumes',Key={'Email' : {'S': 'lightsituma@gmail.com'}})

item = response.get('Item')

print(item)


##############################################################################

