# Ex. 1: Criar uma crud de Animal e seu Dono
# Criar uma classe chamada Dono com os seguintes atributos abaixo:
#   - Nome
#   - CPF
# Criar uma classe chamada Animal com os seguintes atributos abaixo:
# - Raça
# - Dono
# - Data de Nascimento
# Fazer o CR(Create/Read) do Animal solicitando os dados de seu dono também
# Ex. 2: Modificar o conteúdo da classe Dono acrescentando os atributos abaixo:
# -  Bairro, Rua, Número
# Alterar o CR(Create/Read) para solicitar os novos dados do dono
# Modificar o conteúdo da classe Animal acrescentando os atributos abaixo:
#   Peso
#   Altura
#   Sexo
#   Cor
#   Origem da Raça

from ast import List
from datetime import date
import os
import platform
import questionary
from rich.table import Table
from rich.console import Console



class Dono:
    def __init__(self):
        self.nome:str = None
        self.cpf:int = None


class Animal:
    def __init__(self):
        self.raca:str = None
        self.nome_dono: Dono = None
        self.data_nascimento: date = None

console=Console()

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("cls")


def crud_animais():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).aks().lower()
        limpar_tela()

        if menu == "adicionar":
            adicionar()
        elif menu == "listar":
            listar()
def adicionar():
    
    dono = Dono()
    dono.nome = questionary.text("Digite o nome do Dono do animal").ask()
    dono.cpf = float(questionary.text("Digite o cpf").ask())

    animal = Animal()
    animal.nome = questionary.text("Digite o nome do Animal").ask()
    animal.nome_dono = dono
    animal.data_nascimento = questionary.text("Digite a data de nascimento").ask()

    dono.append(dono)
    animal.append(animal)
    console.print("Animal cadastrado com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()

def listar():
    #listar desenvolvedoras
    console.print(Aling.center("Cadastro de desenvolvedora"), style="blue") # type: ignore
    if len(animal,dono) == 0:
        console.print("Nenhuma desenvolvedoras cadastrada", style="red")
        input("Pressione ENTER para continuar ... ")
        limpar_tela()
        return
    colunas = ["Nome do Animal","Data de Nascimento","Nome do dono", "CPF"]
    table = Table(*colunas)

    for i in range(0, len(animal,dono)):
        animal = animal[i]
        dono = dono[i]
        table.add_row(
            animal.nome,
            str(animal.data_nascimento),
        animal.nome_dono.nome,
        str(dono.cpf)
        )

    
    console.print(table)