from ast import List
from datetime import date
import os
import platform
import questionary
from rich.table import Table
from rich.console import Console


class Cachorro:
    #Construtor com 4 parâmetros (3 parâmetros sem valor default e 1 com valor default)
    def __init__(self, raca_param:str, peso: float, idade: int, cor: str = "Carmelo" ):
        #Atributos são preenchidos com os dados dos parâmetros
        #O parâmetro cor tem um valor default(padrão) que é "Caramelo"
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor
        #Atributo com valor pré-definido
        self.cidade_natal = "Blumenau"

def exemplo_construtor_cachorro():
    #Cachorro(raca,peso,idade)
    tobby = Cachorro("Dobberman", 45.20, 15, "Preto")
    print("raça:", tobby.raca)
    print("peso:", tobby.peso)
    print("idade:", tobby.idade)
    print("cidade natal:", tobby.cidade_natal)
    print("cor:", tobby.cor)
    
    daschund = Cachorro("Salsicha", 70.00, 5,)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)
    print("cor:", daschund.cor)




# -------------------------------------------------------------------------------------------
# Exercício de Construtores
# Criar uma classe chamada Passagem com um construtor que contenha os parâmetros abaixo:
# - destino
# - quantidade dias
# - data inicio
# Instanciar dois objetos para desinos diferentes, preenchendo os parâmetros
# Apresentar os dados em uma tabela
# Adicionar os parâmetros abaixo no construtor da classe Passagem
# - quantidade pessoas com valor default 2
# - partida çom valor default 'São Paulo'
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas
# Apresentar na tabela tbm o novo objeto
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas, partida
# Apresentar na tabela tbm o novo objeto

class Passagem:
    def __init__(self, destino: str, quantidade_dias: int, data_inicio: date, quantidade_pessoas: int = 2, partida: str = "São Paulo"):
        self.destino = destino
        self.quantidade_dias = quantidade_dias
        self.data_inicio = data_inicio
        self.quantidade_pessoas = quantidade_pessoas
        self.partida = partida

def exercicio_construtor01():
     
    viagem01 = Passagem("Itália", 20, date(2026, 5, 15), 5)
    viagem02 = Passagem("Grécia", 5, date(2026, 3, 2), 4, "Navegantes")
    viagem03 = Passagem("Tóquio", 60, date(2026, 12, 5),)

    colunas = ["Destino", "Quantidade de dias", "Data de inicio", "Quantidades de Pessoas", "Partida"]
    
    tabela = Table(*colunas)

    tabela.add_row(
         viagem01.destino, str(viagem01.quantidade_dias),str(viagem01.data_inicio), str(viagem01.quantidade_pessoas),viagem01.partida
            )
    tabela.add_row(
         viagem02.destino, str(viagem02.quantidade_dias),str(viagem02.data_inicio), str(viagem02.quantidade_pessoas),viagem02.partida
            )
    tabela.add_row(
         viagem03.destino, str(viagem03.quantidade_dias),str(viagem03.data_inicio), str(viagem03.quantidade_pessoas),viagem03.partida
            )
    
    console = Console()
    console.print(tabela)  

#exercicio_construtor01()