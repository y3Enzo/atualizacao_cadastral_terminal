import json
import os
from dotenv import load_dotenv

load_dotenv()

JSON_PATH = os.getenv("CAMINHO_SOLICITACOES")


def carregar_solicitacoes():
    if not JSON_PATH or not os.path.exists(JSON_PATH):
        print(f"Erro: Arquivo {JSON_PATH} não encontrado.")
        return []

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            solicitacoes = json.load(file)
            return solicitacoes

    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está inválido ou vazio.")
        return []


def visualizar_solicitacao(indice=0):
    solicitacoes = carregar_solicitacoes()

    if (
        not solicitacoes
        or indice < 0
        or indice >= len(solicitacoes)
    ):
        print("Nenhuma solicitação encontrada nesse índice.")
        return

    sol = solicitacoes[indice]

    print("\n" + "=" * 50)
    print("        SOLICITAÇÃO DE ATUALIZAÇÃO")
    print("=" * 50)

    print(f"Cliente:        {sol.get('cliente', 'N/A')}")
    print(f"Tipo:           {sol.get('tipo', 'N/A')}")
    print(f"Status:         {sol.get('status', 'N/A')}")
    print(f"Criado por:     {sol.get('criado_por', 'N/A')}")

    print("-" * 50)

    print(f"Dados antigos:  {sol.get('dados_antigos', 'N/A')}")
    print(f"Dados novos:    {sol.get('dados_novos', 'N/A')}")

    print("=" * 50 + "\n")


def consultar_historico(indice=0):
    solicitacoes = carregar_solicitacoes()

    if (
        not solicitacoes
        or indice < 0
        or indice >= len(solicitacoes)
    ):
        print("Nenhuma solicitação encontrada nesse índice.")
        return

    sol = solicitacoes[indice]
    historico = sol.get("historico", [])

    print("\n" + "=" * 50)
    print(f"HISTÓRICO DA SOLICITAÇÃO - {sol.get('cliente', 'N/A')}")
    print("=" * 50)

    if not historico:
        print("Nenhum histórico registrado.")

    else:
        for numero, item in enumerate(historico, start=1):
            acao = item.get("acao", "N/A")
            usuario = item.get("usuario", "N/A")
            status = item.get("status", "N/A")

            print(f"\n{numero}. Ação: {acao}")
            print(f"   Usuário: {usuario}")
            print(f"   Status: {status}")
            print("-" * 50)

    print("=" * 50 + "\n")


if __name__ == "__main__":
    visualizar_solicitacao(0)
    consultar_historico(0)