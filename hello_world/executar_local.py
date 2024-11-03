
import boto3
from botocore.exceptions import ClientError


# Inicializa o cliente do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',  endpoint_url='http://localhost:8000')  # Altere para a sua região

# Nome da tabela
table_name = "mailing-automatico"  # Substitua pelo nome da sua tabela



def inserir_item(item):
    # Obtém a tabela
    table = dynamodb.Table(table_name)

    try:
        # Insere o item na tabela
        response = table.put_item(Item=item)
        print("Item inserido com sucesso:", response)
    except ClientError as e:
        print("Erro ao inserir item:", e.response['Error']['Message'])

# Exemplo de uso
novo_item = {
    'ID': '123',  # Chave primária
    'nome': 'Produto A',
    'preco': 29,
    'em_estoque': True
}

inserir_item(novo_item)
