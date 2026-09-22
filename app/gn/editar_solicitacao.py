from dados.solicitacoes import solicitacoes

def editar_solicitacao(id_da_solicitacao, acesso):
    lista_de_solicitacoes = solicitacoes.abrir_solicitacoes()

    for solicitacao in lista_de_solicitacoes:
        if not id_da_solicitacao == solicitacao['id']:
            continue

        print(f"ID: {solicitacao['id']}")

        cliente = input(f"Cliente (salvo: {solicitacao['cliente']}): ").strip()
        if cliente:
            solicitacao['cliente'] = cliente

        tipo = input(f"Tipo (salvo: {solicitacao['tipo']}): ").strip()
        if tipo:
            solicitacao['tipo'] = tipo

        print(f"Criado por: {solicitacao['criado_por']}")

        dados_antigos = input(f"Dados antigos (salvo: {solicitacao['dados_antigos']}): ").strip()
        if dados_antigos:
            solicitacao['dados_antigos'] = dados_antigos

        dados_novos = input(f"Dados novos (salvo: {solicitacao['dados_novos']}): ").strip()
        if dados_novos:
            solicitacao['dados_novos'] = dados_novos

        print(f"Histórico (salvo: {solicitacao['historico']})")

        solicitacao['status'] = "AGUARDANDO_GA"

        solicitacao['historico'].append({
            "acao": "editado",
            "usuario": acesso.get('usuario'),
            "status": "AGUARDANDO_GA"
        })

        solicitacoes.salvar_solicitacao(lista_de_solicitacoes)
        print("Solicitação atualizada com sucesso!")
        return

    print("Solicitação não encontrada.")


def listar_solicitacoes():
    """Exibe todas as solicitações cadastradas de forma simplificada."""
    lista = solicitacoes.abrir_solicitacoes()

    if not lista:
        print("Nenhuma solicitação encontrada.")
        return

    print("\n--- LISTA DE SOLICITAÇÕES ---")
    for sol in lista:
        print(f"ID: {sol['id']} | Cliente: {sol['cliente']} | Tipo: {sol['tipo']} | Status: {sol['status']}")
    print("-" * 30)


def visualizar_solicitacao(id_da_solicitacao):
    """Exibe os detalhes completos de uma solicitação específica, incluindo o histórico."""
    lista = solicitacoes.abrir_solicitacoes()

    for sol in lista:
        if sol['id'] == id_da_solicitacao:
            print("\n--- DETALHES DA SOLICITAÇÃO ---")
            print(f"ID: {sol['id']}")
            print(f"Cliente: {sol['cliente']}")
            print(f"Tipo: {sol['tipo']}")
            print(f"Criado por: {sol['criado_por']}")
            print(f"Dados Antigos: {sol['dados_antigos']}")
            print(f"Dados Novos: {sol['dados_novos']}")
            print(f"Status Atual: {sol['status']}")
            
            print("\nHistórico de Alterações:")
            for item in sol.get('historico', []):
                print(f" - Ação: {item.get('acao')} | Usuário: {item.get('usuario')} | Status: {item.get('status')}")
            return

    print("Solicitação não encontrada.")


def alterar_status_solicitacao(id_da_solicitacao, novo_status, acesso):
    """Altera o status de uma solicitação (ex: APROVADO, REPROVADO, CANCELADO)."""
    lista = solicitacoes.abrir_solicitacoes()

    for sol in lista:
        if sol['id'] == id_da_solicitacao:
            sol['status'] = novo_status
            sol['historico'].append({
                "acao": f"status alterado para {novo_status}",
                "usuario": acesso.get('usuario'),
                "status": novo_status
            })

            solicitacoes.salvar_solicitacao(lista)
            print(f"Solicitação {id_da_solicitacao} atualizada para o status: {novo_status}")
            return

    print("Solicitação não encontrada.")
