import sqlite3

def obter_conexao():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    return (conexao, cursor)

def criar_banco():
    conexao, cursor = obter_conexao()
    with open('schema.sql', 'r', encoding='utf-8') as schema:
        schema_sql = schema.read()

    cursor.executescript(schema_sql)
    conexao.commit()
    conexao.close()

    print('Conexão obtida com sucesso!')

criar_banco()