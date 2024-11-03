## Criar banco de dados DynamoDB


## Criar fila localmente na aws
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name gravar-mailing-automatico-sqs

## Posta mensagem na fila aws
aws --endpoint-url=http://localhost:4566 sqs send-message --region us-east-1 --queue-url "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/gravar-mailing-automatico-sqs"  --message-body file://mensagem.json

