import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

CAMINHO_BANCO_DB = os.getenv('CAMINHO_BANCO_DB')
CAMINHO_SCHEMA_SQL = os.getenv('CAMINHO_SCHEMA_SQL')

def obter_conexao():
    conexao = sqlite3.connect(CAMINHO_BANCO_DB)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    return (conexao, cursor)

def criar_banco():
    conexao, cursor = obter_conexao()
    with open(CAMINHO_SCHEMA_SQL, 'r', encoding='utf-8') as schema:
        schema_sql = schema.read()

    cursor.executescript(schema_sql)
    conexao.commit()
    conexao.close()

    print('Conexão obtida com sucesso!')

criar_banco()