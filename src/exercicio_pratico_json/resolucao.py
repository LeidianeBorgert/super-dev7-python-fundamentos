from typing import Dict, List
from src.arquivos import ler_json,escrever_json
from rich.console import Console
from rich.table import Table

def resolver():
    # Pegar os dados de algum lugar:
    # - Arquivo => leitura do arquivo
    # - Pegar todos que estão ativos
    #     - Pegar status
    #     - Pegar nome
    #     - Pegar e-mail
    #     - Pegar tipo
    #     - Pegar plano
    #     - Pegar pontuação
    #     - Adicionar o dado consolidado na lista
    # - Salvar o arquivo

    #Ler o arquivo e converterndo para uma lista de dicionário
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta")
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura",{})
        plano = assinatura.get("plano","Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")
        email = dados_pessoais.get("email")

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano
        }

        if status == "ativo":
            #print(nome, "Ativo")
            ativos.append(dados) #colocar um registro dentro da lista
        elif status == "suspenso":
            #print (nome, "Suspenso")
            suspensos.append(dados)
        else:
            #print(nome, "Inativo")
            inativos.append(dados)

        escrever_json(ativos, "data/ativos.json")
        escrever_json(suspensos, "data/suspensos.json")
        escrever_json(inativos, "data/inativos.json")

        apresentar_tabela(ativos, "Contas Ativas")
        apresentar_tabela(inativos, "Contas Inativas")
        apresentar_tabela(suspensos, "Contas Suspensas")

def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("Email", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")

    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome"),
            dado.get("email"),
            dado.get("tipo"),
            str(dado.get("pontos")),
            dado.get("plano"),
        )

    console = Console()
    console.print(table)


# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free
# Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários
# Exercício 03
#   Percorrer a lista de usuário, armazenando no arquivo 'enderecos.json' todos os endereços dos usuários
# Ex.: ["Rua - Numero - Bairro - CEP - UF", "Rua - Numero - Bairro - CEP - UF"]
# Exercício 04:
#   Percorrer a lista de usuários agrupando os dados por estado, salvando o telefone e e-mail de cada usuário em uma lista por estado. 
# Deve armazenar uma lista com os usuários conforme abaixo:
#   Ex.: sc.json
#       [{"email": "elisa.rocha@example.com", "telefone": "......"}]


def exercicio_01():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    free = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        dados_pessoais =usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")

        assinatura = usuario.get("assinatura")
        plano = assinatura.get("plano")

        dados = {
        "nome": nome,
        "plano": plano
        }

        if plano == "Free":
            free.append(dados)


    escrever_json(free, "data/free.json")
    apresentar_tabela(free, "Contas com Plano Free")

def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome")
    table.add_column("Plano")

    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome"),
            dado.get("plano"),
        )

    console = Console()
    console.print(table)   


def exercicio_02():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")
    tag = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        tags = usuario.get("tags",[])
       
        dados = {    
            "tags":tags
        }

        tag.append(dados)
        
    escrever_json(tag, "data/tag.json")

    print(tag)




        


