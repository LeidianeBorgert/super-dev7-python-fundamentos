from typing import List
from datetime import date
import os
import platform
import questionary
from rich.table import Table
from rich.console import Console


class Aluno:
    def __init__(
            self, 
            nome: str, 
            notas: List[float],
            frequencia: float = 75,
            turma: str = "SuperDev"
    ):
        self.nome = nome
        self.notas = notas
        self.fequencia = frequencia
        self.turma = turma

def exemplo_passagem_parametros_nomeados():
    #Pedro terá a frequencia de 75%, pq foi utilizado o valor default do
    # parâmetro de frequencia
    #nome(turma)

    pedro = Aluno(
        "Pedro Silva", 
        [8, 7, 6.5], 
        turma="SuperDev 7ª"
        )
     
    #Passando todos os parâmetros pelo nome, podendo passar em qualquer ordem

    maria = Aluno(
        notas=[10, 9.75, 3],
        nome = "Maria",
        turma="Adas",
        frequencia=100,
        )

# ------------------------------------------------------------------------------
# Exercício de métodos com parâmetros nomeados
# Criar uma classe chamada Player com os seguintes parâmetros no construtor
# nick com valor default "Geraldão"
# classe com valor default "tanque"
# lane com valor default "meio"
# elo com valor default "bronze"
# maestria com valor default "7"
# main com valor default "Jinx"
# N utilizar os mesmos atributos, mudar a cada instancia nova (utilizar outros)
# Instanciar um objeto com 3 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Instanciar um objeto com 1 atributo noemado
# Instanciar um objeto com 5 atributos noemados
# Instanciar um objeto com 4 atributos noemados
# Instanciar um objeto com 6 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Apresentar os dados
# 
# Ex 2: Criar uma classe com 4 parâmetros alguns com valores defaults e outros n
# Instanciar objetos e apresentar
# 
# Ex 3: Criar uma classe com 10 parâmetros alguns com valores defaults 
# e outros n
# Instanciar objetos e apresentar

class Player:
    def __init__(
            self,
            nick:str = "Geraldão",
            classe:str = "tanque",
            lane:str = "meio",
            elo:str = "bronze",
            maestria:int = 7,
            main:str = "Jinx"
         ):
        self.nick = nick
        self.classe = classe
        self.lane = lane
        self.elo = elo
        self.maestria = maestria
        self.main = main

def nomear_player():
 # Instanciar um objeto com 3 atributos noemados
    player01 = Player( 
            nick = "Geraldão",
            classe = "tanque",
            lane = "meio",
            elo = "ouro",
            maestria= 9,
            main = "Fenix")
# Instanciar um objeto com 2 atributos noemados   
    player02 = Player( 
            nick = "Geraldão",
            classe = "tanque",
            lane = "frente",
            elo = "prata",
            maestria = 10,
            main = "Moon")

# Instanciar um objeto com 1 atributo noemado
    player03 = Player( 
            nick = "Geraldão",
            classe = "ferro",
            lane = "lado",
            elo = "prata",
            maestria = 5,
            main = "Saturno")
# Instanciar um objeto com 5 atributos noemados
    player04 = Player( 
            nick = "Geraldão",
            classe = "tanque",
            lane = "meio",
            elo = "bronze",
            maestria = 10,
            main = "Jinx")

# Instanciar um objeto com 4 atributos noemados
    player05 = Player( 
            nick = "Geraldão",
            classe = "tanque",
            lane = "meio",
            elo = "ouro",
            maestria = 6,
            main = "Jinx")

# Instanciar um objeto com 6 atributos noemados
    player06 = Player( 
            nick = "Geraldão",
            classe = "tanque",
            lane = "meio",
            elo = "bronze",
            maestria = 10,
            main = "Jinx")

    colunas = ["Nick", "Classe", "Lane", "Elo", "Maestria", "Main"]
    
    tabela = Table(*colunas)

    tabela.add_row(
         player01.nick, player01.classe,player01.lane,player01.elo, str(player01.maestria),player01.main
            )
    tabela.add_row(
         player02.nick, player02.classe,player02.lane,player02.elo, str(player02.maestria),player02.main
            )
    tabela.add_row(
         player03.nick, player03.classe,player03.lane,player03.elo, str(player03.maestria),player03.main
            )
    tabela.add_row(
         player04.nick, player04.classe,player04.lane,player04.elo, str(player04.maestria),player04.main
            )
    tabela.add_row(
         player05.nick, player05.classe,player05.lane,player05.elo, str(player05.maestria),player05.main
            )
    tabela.add_row(
         player06.nick, player06.classe,player06.lane,player06.elo, str(player06.maestria),player06.main
            )
    
    
    console = Console()
    console.print(tabela)  


# Ex 2: Criar uma classe com 4 parâmetros alguns com valores defaults e outros n
# Instanciar objetos e apresentar
# Livro
# título, 
# autor, 
# paginas (default), 
# gênero (default)

class Livros():
    def __init__(
            self,
            titulo:str,
            autor:str = "Machado de Assis",
            paginas:int = 400,
            genero:str = "Literatura Brasileira"
        ):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero

def exercicio02():
    livro01 = Livros(            
            titulo = "O Hobbit" ,
            autor = "J.R.R.Tolkien",
            paginas = 320,
            genero = "Alta fantasia")
    
    livro02 = Livros(            
            titulo = "A Guerra da Papoula" ,
            autor = "R. F. Kuang",
            paginas = 512,
            )
    livro03 = Livros(            
            titulo = "Mistborn: O Herói das Eras" ,
            paginas = 800,
            genero = "Alta fantasia")
    livro04 = Livros(            
            titulo = "Ritmo da Guerra: Livro 4" ,
            autor = "Brandon Sanderson",
          )
    livro05 = Livros(            
            titulo = "Yumi e o pintor de pesadelos" ,
            autor = "Brandon Sanderson",
            paginas = 552,
            genero = "Alta fantasia")
    
    colunas = ["Titulo", "Autor", "Páginas", "Genero"]
    
    tabela = Table(*colunas)

    tabela.add_row(
         livro01.titulo, livro01.autor,str(livro01.paginas),livro01.genero
            )
    tabela.add_row(
         livro02.titulo, livro02.autor,str(livro02.paginas),livro02.genero
            )
    tabela.add_row(
         livro03.titulo, livro03.autor,str(livro03.paginas),livro03.genero
            )
    tabela.add_row(
         livro04.titulo, livro04.autor,str(livro04.paginas),livro04.genero
            )
    tabela.add_row(
         livro05.titulo, livro05.autor,str(livro05.paginas),livro05.genero
            )
    
    
    
    
    
    console = Console()
    console.print(tabela)  
   

# Ex 3: Criar uma classe com 10 parâmetros alguns com valores defaults 
# e outros n
# Instanciar objetos e apresentar 
# Personagem de RPG 
# nome, 
# classe, str
# nível, 1 a 10
# vida, 1 a 300
#magia str 
# mana 1 a 100
# força, 1 a 300
# agilidade, baixa media alta
# raça, 
# arma

class Personagem():
    def __init__(
            self,
            id:int,
            nome:str,
            classe:str,
            nivel:int ,
            vida:int = 60,
            magia:str ="Paralisar",
            mana:int = 50,
            forca:int = 50 ,
            agilidade:str = "Baixa",
            raca:str = "Humano", 
            arma:str = "Punhal",
            ):
        self.id = id
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.magia = magia
        self.mana = mana
        self.forca = forca
        self.agilidade = agilidade
        self.raca = raca
        self.arma = arma

def exercicio03():

    personagem01 = Personagem(
        id = 1,
        nome ="Miriel",
        classe ="Feiticeira",
        nivel = 8,
        vida = 250,
        magia = "Magia Negra",
        mana = 30,
        forca = 150,
        agilidade = "Média", 
        arma ="Cajado Cristalino"
        )
    personagem02 = Personagem(
        id = 2,
        nome ="Kael",
        classe ="Paladino",
        nivel = 3,
        vida = 100,
        mana = 60,
        forca = 90,
        agilidade = "Baixa",
        arma ="Martelo Sagrado"
        )
    personagem03 = Personagem(
        id = 3,
        nome ="Thorgar",
        classe ="Bárbaro",
        nivel = 5,
        vida = 300,
        magia = "Escudo de Mana",
        mana = 40,
        forca = 250,
        agilidade = "Alta",
        raca = "Orc", 
        )
    personagem04 = Personagem(
        id = 4,
        nome ="Seraphine",
        classe ="Clériga",
        nivel = 7,
        vida = 120,
        magia = "Teleporte",
        mana = 60,
        forca = 200,
        agilidade = "Alta",
        raca = "Anã das Montanhas Azuis", 
        arma ="Maça Sagrada"
        )
    personagem05 = Personagem(
        id = 5,
        nome ="Ragnor",
        classe ="Berserker",
        nivel = 10,
        vida = 300,
        magia = "Armadura Elemental",
        mana = 100,
        forca = 300,
        agilidade = "Alta",
        raca = "Meio-Gigante ", 
        arma ="Machado Duplo"
        )
    personagem06 = Personagem(
        id = 6,
        nome ="Thalia",
        classe ="Druida",
        nivel = 9,
        vida = 250,
        magia = "Barreira Mágica",
        mana = 50,
        forca = 100,
        agilidade = "Baixa",
        raca = "Elfa Silvestre", 
        arma ="Cajado Natural"
        )
    personagem07 = Personagem(
        id = 7,
        nome ="Arwyn",
        classe ="Patrulheira",
        nivel = 6,
        vida = 90,
        magia = "Cura",
        mana = 30,
        forca = 70,
        agilidade = "Média",
        raca = "Elfa da Floresta", 
        arma ="Arco de Carvalho"
        )
     
    colunas = ["ID", "Nome", "Classe", "Nível", "Vida", "Magia", "Mana", 
               "Força", "Agilidade", "Raça", "Arma"]
    
    tabela = Table(*colunas)

    tabela.add_row(
        str(personagem01.id), personagem01.nome, personagem01.classe, 
        str(personagem01.nivel), str(personagem01.vida), personagem01.magia, 
        str(personagem01.mana), str(personagem01.forca), personagem01.agilidade,
        personagem01.raca, personagem01.arma)
    tabela.add_row(
        str(personagem02.id), personagem02.nome, personagem02.classe, 
        str(personagem02.nivel), str(personagem02.vida), personagem02.magia, 
        str(personagem02.mana), str(personagem02.forca), personagem02.agilidade,
        personagem02.raca, personagem02.arma)
    tabela.add_row(
        str(personagem03.id), personagem03.nome, personagem03.classe, 
        str(personagem03.nivel), str(personagem03.vida), personagem03.magia, 
        str(personagem03.mana), str(personagem03.forca), personagem03.agilidade,
        personagem03.raca, personagem03.arma)
    tabela.add_row(
        str(personagem04.id), personagem04.nome, personagem04.classe, 
        str(personagem04.nivel), str(personagem04.vida), personagem04.magia, 
        str(personagem04.mana), str(personagem04.forca), personagem04.agilidade,
        personagem04.raca, personagem04.arma)
    tabela.add_row(
        str(personagem05.id), personagem05.nome, personagem05.classe, 
        str(personagem05.nivel), str(personagem05.vida), personagem05.magia, 
        str(personagem05.mana), str(personagem05.forca), personagem05.agilidade,
        personagem05.raca, personagem05.arma)
    tabela.add_row(
        str(personagem06.id), personagem06.nome, personagem06.classe, 
        str(personagem06.nivel), str(personagem06.vida), personagem06.magia, 
        str(personagem06.mana), str(personagem06.forca), personagem06.agilidade,
        personagem06.raca, personagem06.arma)
    tabela.add_row(
        str(personagem07.id), personagem07.nome, personagem07.classe, 
        str(personagem07.nivel), str(personagem07.vida), personagem07.magia, 
        str(personagem07.mana), str(personagem07.forca), personagem07.agilidade,
        personagem07.raca, personagem07.arma)


    
    console = Console()
    console.print(tabela)  
exercicio03()
   
    
