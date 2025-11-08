from typing import Dict, Union

def exemplo_dicionario_basico():
    #Dicionário é uma formar de armazenar chaves e valores
    #Cada chave está atrelado a um valor

    #Dicionário terá uma chave do tipo string
    #Pode armazenar string, int ou bool
    #Criarmos um dicionário com 2 chaves (apelido,idade)

    cachorro: Dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True,
        "peso": 22.5,
    }

    #Acrescentar uma nova chave com um valor
    cachorro["raca"] = "Pastor Alemão"

    cachorro["cor"] = "Caramelo"

    #Alterar o valor de uma chave
    cachorro["idade"] = 5

    #Remover uma chave(automaticamente remove o valor)
    cachorro.pop("abandonado")

    #print("Cachorro:", cachorro["apelido"])
    print(f"""
Cachorro: {cachorro.get("apelido")}
Raça: {cachorro.get("raca")}
Idade: {cachorro.get("idade")}
Cor: {cachorro.get("cor")}
Abandonado: {cachorro.get("abandonado")}
Peso: {cachorro.get("peso")}
        """)

#-----------------------------------------Execício 01:
#Criar uma função exemplo_dicionario_aluno
#Criar um dicionário chamado aluno com os seguintes dados
# nome_completo
# nome_mae
# nome_pai
# jogar(true)
#Apresentar os dados do dicionário
#Adicionar a chave idade do aluno
#Apresentar a idade do aluno
#Alterar a idade do aluno para +1
#Remover a chave jogar do aluno
#Apresentar os dados

def exemplo_dicionario_aluno():

    aluno: Dict[str, Union[str, int, bool, float]] = {
        "nome_completo": "Ana Luiza de Souza",
        "nome_mae": "Ângela Conceição de Souza",
        "nome_pai": "Arnaldo de Souza",
        "jogar": True,
    }

    #Adicionar a chave idade do aluno
    aluno["idade"] = 14

    #Alterar a idade do aluno para +1
    aluno["idade"] = 15

    #Remover a chave jogar do aluno
    aluno.pop("jogar")


    print(f"""
Nome do(a) aluno(a): {aluno.get("nome_completo")}
Nome da Mãe: {aluno.get("nome_mae")}
Nome do Pai: {aluno.get("nome_pai")}
Idade: {aluno.get("idade")}
Joga: {aluno.get("jogar")}
         """)
