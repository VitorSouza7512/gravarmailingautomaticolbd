import boto3
from botocore.exceptions import ClientError

# Inicializa o cliente do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',  endpoint_url='http://localhost:8000')  # Altere para a sua região

# Nome da tabela
table_name = "mailing-automatico"  # Substitua pelo nome da sua tabela

def listar_dados():
    # Obtém a tabela
    table = dynamodb.Table(table_name)

    try:
        # Inicializa uma lista para armazenar todos os itens
        dados = []

        # Realiza o scan para obter todos os itens da tabela
        response = table.scan()

        # Adiciona os itens da primeira página
        dados.extend(response.get('Items', []))

        # Continua a buscar enquanto houver mais dados (paginação)
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            dados.extend(response.get('Items', []))

        # Retorna todos os dados obtidos
        return dados

    except ClientError as e:
        print("Erro ao listar dados:", e.response['Error']['Message'])
        return None


# Chama a função e imprime os dados
dados_tabela = listar_dados()
if dados_tabela:
    for item in dados_tabela:
        print(item)
