

import boto3
from botocore.exceptions import ClientError

# Inicializa o cliente do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',  endpoint_url='http://localhost:8000')  # Altere para a sua região

# Nome da tabela
table_name = "mailing-automatico"  # Substitua pelo nome da sua tabela

def deletar_todos_itens():
    # Obtém a tabela
    table = dynamodb.Table(table_name)

    try:
        # Usa scan para listar todos os itens
        response = table.scan()
        items = response.get('Items', [])

        # Loop para deletar cada item individualmente
        with table.batch_writer() as batch:
            for item in items:
                batch.delete_item(Key={'ID': item['ID']})  # Substitua 'id' pela chave primária correta

        print("Todos os itens foram deletados com sucesso.")

    except ClientError as e:
        print("Erro ao deletar itens:", e.response['Error']['Message'])

# Executa a função
deletar_todos_itens()
