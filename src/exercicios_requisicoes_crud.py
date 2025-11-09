from typing import Dict, List
import questionary
import requests
from rich.console import Console
from rich.table import Table
import os
import platform

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def crud_eventos():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha no menu", choices=[
            "Evento",  "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Evento":
            menu_evento()

def menu_evento():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu", choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Listar":
            listar_eventos()
        elif opcao == "Cadastrar":
            cadastrar_evento()
        elif opcao == "Excluir":
            exluir_evento()
        elif opcao == "Editar":
          editar_evento()

def listar_eventos():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/eventos"
    response = requests.get(url)
    if response.status_code == 200:
        eventos: List[Dict[str, str | float | int]] = response.json()
        quantidade_eventos = len(eventos)

        tabela = Table()
        tabela.add_column("Código")
        tabela.add_column("Título")
        tabela.add_column("Local")
        tabela.add_column("Custo")

        
        for i in range(0, quantidade_eventos):
            evento = eventos[i] # pegar da lista o evento por uma posição
            titulo = evento.get("titulo")
            id = evento.get("id")
            local = evento.get("local")
            custo = evento.get("custo")

            tabela.add_row(str(id), titulo,local, f"R$ {custo}")
            
        console = Console()
        console.print(tabela)


def cadastrar_evento():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/eventos"
    titulo = questionary.text("Digite o titulo do evento").ask().strip()
    local = questionary.text("Digite o local do evento").ask()
    custo_evento = float(questionary.text("Digite o custo do evento").ask().replace(",", "."))
    payload = {
        "titulo": titulo,
        "local": local,
        "custo": custo_evento
    }
    headers = {
        "Content-Type": "application/json-patch+json"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Evento cadastrado com sucesso")
    else:
        print("Ocorreu uma falha ao cadastrar o evento\nErro:", response.text)

def exluir_evento():
    listar_eventos()
    id = questionary.text("Digite o id para apagar o evento").ask()

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/eventos/{id}"

    response = requests.delete(url)

    if response.status_code == 204:
        print("Evento excluído com sucesso")
    elif response.status_code == 404:
        print("Evento não encontrado")
    else:
        print(f"Não foi possível apagar o evento. Erro:{response.text}")

def editar_evento():
    listar_eventos()

    id_para_editar = questionary.text("Digite o id para editar o evento").ask()
    titulo = questionary.text("Digite o titulo do evento").ask().strip()
    local = questionary.text("Digite o local do evento").ask()
    custo_evento = float(questionary.text("Digite o custo do evento").ask().replace(",", "."))

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/eventos/{id_para_editar}"

    payload = {
        "titulo": titulo,
        "local": local,
        "custo": custo_evento
    }
    
    headers = {
        "Content-Type": "application/json-patch+json"
    }
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Evento alterado com sucesso")
    else:
        print("Ocorreu uma falha ao alterar o evento\nErro:", response.text)




if __name__ == "__main__":
    crud_eventos()