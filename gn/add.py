from dados.solicitacoes.solicitacoes import abrir_solicitacoes


def consultar_solicitacao(id_solicitacao):
    solicitacoes = abrir_solicitacoes()

    for solicitacao in solicitacoes:
        if solicitacao["id"].upper() == id_solicitacao.upper():
            print(f"ID: {solicitacao['id']}")
            print(f"Cliente: {solicitacao['cliente']}")
            print(f"Tipo: {solicitacao['tipo']}")
            print(f"Status: {solicitacao['status']}")
            print(f"Criado por: {solicitacao['criado_por']}")
            print(f"Dados antigos: {solicitacao['dados_antigos']}")
            print(f"Dados novos: {solicitacao['dados_novos']}")
            print(f"Histórico: {solicitacao['historico']}")
            return solicitacao

    print(f"Solicitação {id_solicitacao} não foi encontrada!")
    return None