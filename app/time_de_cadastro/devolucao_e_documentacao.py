import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from dados.solicitacoes.solicitacoes import (
    abrir_solicitacoes,
    salvar_solicitacao
)


def devolver_para_ga(numero_solicitacao):
    solicitacoes = abrir_solicitacoes()

    indice = numero_solicitacao - 1

    if indice < 0 or indice >= len(solicitacoes):
        print("Solicitação não encontrada.")
        return

    solicitacao = solicitacoes[indice]

    solicitacao["status"] = "DEVOLVIDA_AO_GA"
    solicitacao["destino"] = "GA"

    solicitacao["historico"].append({
        "acao": "Devolução para ajuste",
        "usuario": "GN",
        "status": "DEVOLVIDA_AO_GA"
    })

    salvar_solicitacao(solicitacoes)

    print("Solicitação devolvida para o GA.")


def devolver_para_gn(numero_solicitacao):
    solicitacoes = abrir_solicitacoes()

    indice = numero_solicitacao - 1

    if indice < 0 or indice >= len(solicitacoes):
        print("Solicitação não encontrada.")
        return

    solicitacao = solicitacoes[indice]

    solicitacao["status"] = "DEVOLVIDA_AO_GN"
    solicitacao["destino"] = "GN"

    solicitacao["historico"].append({
        "acao": "Devolução para ajuste",
        "usuario": "GA",
        "status": "DEVOLVIDA_AO_GN"
    })

    salvar_solicitacao(solicitacoes)


def registrar_documento(id_solicitacao, documento, usuario_logado):
    solicitacoes = abrir_solicitacoes()
    solicitacao = None

    for solicitacao_ in solicitacoes:
        if solicitacao_.get('id') != id_solicitacao:
            continue

        solicitacao = solicitacao_
        break

    if "documentos" not in solicitacao:
        solicitacao["documentos"] = []

    solicitacao["documentos"].append(documento)

    solicitacao["historico"].append({
        "acao": "Documento registrado",
        "usuario": usuario_logado,
        "status": solicitacao["status"]
    })

    salvar_solicitacao(solicitacoes)
    print("Documento registrado com sucesso.")
