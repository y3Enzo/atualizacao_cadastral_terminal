import uuid
import sys #Bibliotecas 
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) #Serve para encontrar arquivos de outra pasta

from dados.solicitacoes import solicitacoes
from dados.banco import Banco, BuscarNoBanco

logger = logging.getLogger(__name__)

class SolicitacaoCadastro:
    def __init__(self, buscador):
        self.id = solicitacoes.obter_proximo_id()
        self.cliente = None
        self.tipo = None
        self.dados_antigos = None
        self.dados_novos = None     #São as listas vazias prontas para receberem informações e guardar elas
        self.criado_por = None
        self.historico = []
        self.status = None
        self._buscador = buscador

    def inserir_dados_novos(self, dados):
        self.dados_novos = dados

    def buscar_cliente(self, identificador): #Identifica pelo nome ou pelo cpf
        
        if not identificador:
            return False

        identificador = str(identificador).strip()

        if identificador.isdigit() and len(identificador) == 11: #Se tiver 11 número sem espaço ele indentifiica como cpf e se tiver espaço identifica como nome 
            self.cliente = self._buscador.buscar_cliente_por_cpf(identificador)
        else:
            self.cliente = self._buscador.buscar_cliente_por_nome(identificador)

        if self.cliente is None:
            return False #Busca o cliente por cpf ou nome se caso o cliente não exista retorna falso

        return True

    def selecionar_tipo(self, opcao): #Tipos de solicitação
        tipos_disponiveis = {
            "1": "Renda",
            "2": "Patrimônio Veículo",
            "3": "Patrimônio Imóvel",
            "4": "Endereço",
        }

        if opcao not in tipos_disponiveis: #Se a opção informada não existir retorna falso
            return False

        self.tipo = tipos_disponiveis[opcao] #Se o tipo existir retorna true
        return True

    def criar_solicitacao(self, usuario_logado):
        self.dados_antigos = None

        match self.tipo:
            case "Renda":
                self.dados_antigos = self.cliente.get('salario')
            case "Patrimônio Veículo":
                self.dados_antigos = self.cliente.get('veiculo')
            case "Patrimônio Imóvel":
                self.dados_antigos = self.cliente.get('endereco')
            case "Endereço":
                self.dados_antigos = self.cliente.get('casa_propria')

        solicitacao = {
            "id": self.id,
            "cliente": self.cliente.get('nome'),
            "tipo": self.tipo,
            "dados_antigos": self.dados_antigos,
            "dados_novos": self.dados_novos,
            "criado_por": usuario_logado.get('usuario'),
            "historico": [
                {
                    "acao": "criada",
                    "usuario": usuario_logado.get('usuario'),
                    "status": "ESPERANDO_GA"
                }
            ],
            "status": "ESPERANDO_GA"
        }

        solicitacoes.adicionar_solicitacao(solicitacao)
        logger.info(f'Solicitação com ID {self.id} criada com sucesso')

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "tipo": self.tipo,
            "dados_antigos": self.dados_antigos,
            "dados_novos": self.dados_novos,
            "criado_por": self.criado_por,
            "historico": self.historico,
            "status": self.status, #Essa parte serve para empacotar todas as informações do pedido e entregá-las em formato de lista/dicionário.
        }
