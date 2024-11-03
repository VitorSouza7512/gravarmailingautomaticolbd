docker run -p 8000:8000 amazon/dynamodb-local

## Comando para criar uma tabela localmente
aws --endpoint-url=http://localhost:8000 dynamodb create-table --table-name mailing-automatico --attribute-definitions AttributeName=ID,AttributeType=S --key-schema AttributeName=ID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --region us-east-1