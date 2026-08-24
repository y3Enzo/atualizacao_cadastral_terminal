import json
from dotenv import load_dotenv
import os

load_dotenv()
CAMINHO_SOLICITACOES= os.getenv("CAMINHO_SOLICITACOES")


def abrir_solicitacoes():
    with open(CAMINHO_SOLICITACOES, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    

def salvar_solicitacao(solicitacoes):
    with open (CAMINHO_SOLICITACOES, "w", encoding="utf-8") as arquivo:
        return json.dump(solicitacoes, arquivo, indent=4, ensure_ascii = False)
    