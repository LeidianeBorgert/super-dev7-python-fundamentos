from ast import List
from datetime import date
import os
import questionary
from rich.table import Table
from rich.console import Console

class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []


#Classe é uma representação do objeto do mundo real 
class Jogo:
    def __init__(self):
        #Atributos da classe
        self.titulo:str = None
        self.data_lancamento: date = None
        self.preco:float = None
        self.genero:str = None
        self.classificacao:str = None
        self.desenvolvedora: Desenvolvedora = None

def exemplo_01():
        # #titulo = "GTV VI"
    # data_lancamento = date(2077, 2, 28)
    # preco = 650.00
    # genero = "Ação"
    # classificacao = "M"


    # gta_vi_dict = {
    #     "titulo": "GTA VI",
    #     "data_lancamento": date(2077, 2 ,28),
    #     "preco": 650.00,
    #     "genero": "Ação",
    #     "classificacao": "M",
    # }


    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New York"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    #Instaciando um objeto chamado gta_vi da classe Jogo
    gta_vi = Jogo()#nome_objeto  = NomeClasse()
    #Definindo valor para as atributos do objeto
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 650
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    gta_vi.preco = 669.99

    the_witcher = Jogo()

    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()
    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10 ,27)
    league_of_legends.preco = 0
    league_of_legends.genero = "Moba"
    league_of_legends.classificacao = "12"

    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)




    colunas = ["Desenvolvedora","Título","Data de Lançamento", "Preço", "Gênero", "Classificação"]
    #Instanciando um objeto chamado tabela da classe Table

    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao
    )
    tabela.add_row(
        "N/A",the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao
    )
    tabela.add_row(
        "N/A",league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificacao
    )

    #Intanciando um obnjeto chamado console de classe Console
    console = Console()
    console.print(tabela)

#Exercicio 01 - criar classe chamada Marca com os seguintes atributos
#nome str
#id (1,2,3,4,5...)
#fundador str
#data de fundação date
#Faturamento float
# criar um função exercicio_marca
# intaciar 2 objetos da classe marca, atribuindo valor para todos os atributos


class Marca:
    def __init__(self):
        self.nome: str = None
        self.id: int = None
        self.fundador: str = None
        self.data_fundacao: date = None
        self.faturamento: float = None

def exercicio_marca():

    sony = Marca()
    sony.nome = "Sony Group"
    sony.id = 1
    sony.fundador = "Masaru Ibuka"
    sony.data_fundacao = date(1946, 5, 7)
    sony.faturamento = 560.000

    jbl = Marca()
    jbl.nome = "JBL"
    jbl.id = 2
    jbl.fundador = "James Bullough Lansing"
    jbl.data_fundacao = date(1946, 10, 1)
    jbl.faturamento = 280.880

    colunas = ["Nome", "Id", "Fundador", "Data de Fundação", "Faturamento"]

    tabela = Table(*colunas)

    tabela.add_row(
         sony.nome,str(sony.id), sony.fundador, str(sony.data_fundacao), str(sony.faturamento)
    )
    tabela.add_row(
         jbl.nome,str(jbl.id), jbl.fundador, str(jbl.data_fundacao), str(jbl.faturamento)
    )

    console = Console()
    console.print(tabela)

# Exercicio 02 criar uma classe chamada Usuario com os seguintes atributos
#  - id (1,2,3,4...)
#  - Nome completo
#  - login
#  - data de nascimento 
# criar uma classe chamada Ticket com os seguintes atributos
#  - número(1000,1001,1002)
#  - usuario do tipo usuario
#  - data de abertura
#  - status
#  - data de fechamento
#  - descrição
#  - criar um função exercico_ticket
# intanciar dois usuarios e preencher os atributos
# criar um ticket para o primeiro usuario com status de em analise preenchendo todas as propriedades com execeção da data 
# de fechamento a data de abertura deve ser hoje
# criar um ticket para o segundo usuario com status de finalizado preenchendo todas as propriedades. a data de abertura deve ser 
# 10 dias atras, a data de fechamento dever ser hoje
# apresentar os dados do Ticket e seus usuarios


class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.login:str = None
        self.data_nascimento: date = None

class Ticket:
    def __init__(self):
        self.numero: int = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao:str = None

def exercicio_ticket():

    usuario01 = Usuario()
    usuario01.nome_completo = "Ana Maria"
    usuario01.id = 1000
    usuario01.login = "ana_maria"
    usuario01.data_nascimento = date(1999, 12, 6)

    usuario02 = Usuario()
    usuario02.nome_completo = "Luiz Silva"
    usuario02.id = 1001
    usuario02.login = "luiz_silva"
    usuario02.data_nascimento = date(2002, 5, 25)


    ticket_usuario01= Ticket()
    ticket_usuario01.numero = 1000
    ticket_usuario01.usuario = usuario01
    ticket_usuario01.data_abertura = date(2025, 11, 12)
    ticket_usuario01.status = "Em analise"
    ticket_usuario01.data_fechamento = date(2025, 11, 22)
    ticket_usuario01.descricao = "Sistema não instalado"

    ticket_usuario02= Ticket()
    ticket_usuario02.numero = 1001
    ticket_usuario02.usuario = usuario02
    ticket_usuario02.data_abertura = date(2025, 11, 2)
    ticket_usuario02.status = "Finalizado"
    ticket_usuario02.data_fechamento = date(2025, 11, 12)
    ticket_usuario02.descricao = "Sistema não instalado"
    

    colunas = ["Número","Usuario","Data de Abertura", "Status", "Data Fechamenti", "Descrição"]
    

    tabela = Table(*colunas)

    tabela.add_row(
       str(ticket_usuario01.numero), ticket_usuario01.usuario.nome_completo, str(ticket_usuario01.data_abertura), ticket_usuario01.status, str(ticket_usuario01.data_fechamento), ticket_usuario01.descricao
    )
    tabela.add_row(
         str(ticket_usuario02.numero), ticket_usuario02.usuario.nome_completo, str(ticket_usuario02.data_abertura), ticket_usuario02.status, str(ticket_usuario02.data_fechamento), ticket_usuario02.descricao
    )
    
    console = Console()
    console.print(tabela)  



def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("cls")


console = Console()
desenvolvedora: List[Desenvolvedora] = []


def explemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).aks().lower()
        limpar_tela()

        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()

def adicionar_desenvolvedora():
    #Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Aling.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietario").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.pais = questionary.text("Digite o país da sede").ask()
    

    desenvolvedora.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    #listar desenvolvedoras

    if len(desenvolvedora) == 0:
        console.print("Nenhuma desenvolvedoras cadastrada", style="red")
        input("Pressione ENTER para continuar ... ")
        limpar_tela()
        return
    
    table = Table("Nome", "Proprietário","Endereço")

    for i in range(0, len(desenvolvedora)):
        desenvolvedora = desenvolvedora[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )
console.print(table)
explemplo_crud_lista_objetos()