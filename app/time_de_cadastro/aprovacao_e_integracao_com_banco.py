import logging
from app.dados.banco import Banco

logger = logging.getLogger(__name__)

def efetivar_solicitacao(solicitacao):
    conexao, cursor = Banco.obter_conexao()
    cliente = solicitacao.get('cliente')
    dados_novos = solicitacao.get('dados_novos')
    tipo = solicitacao.get('tipo')

    match tipo:
        case 'Renda':
            cursor.execute('''
                UPDATE clientes
                SET salario = ?
                WHERE nome = ?''',
                (dados_novos, cliente))
        case 'Patrimônio Veículo':
            cursor.execute('''
                UPDATE clientes
                SET veiculo = ?
                WHERE nome = ?''',
                (dados_novos, cliente))
        case 'Patrimônio Imóvel':
            cursor.execute('''
                UPDATE clientes
                SET endereco = ?
                WHERE nome = ?''',
                (dados_novos, cliente))
        case 'Endereço':
            cursor.execute('''
                UPDATE clientes
                SET casa_propria = ?
                WHERE nome = ?''',
                (dados_novos, cliente))
        case _:
            logger.error(f'Efetivação da solicitacao {solicitacao.get('id')} mal-sucedida: tipo de atualização inválida')
            return
    conexao.commit()
    conexao.close()
    logger.info(f'Solicitação {solicitacao.get('id')} efetivada com sucesso')
