def exemplo_strings():
    #Variáveis do tipo string
    nome_inquilino: str = "Maria"
    sobrenome_inquilino: str = "da Silva"

    #Concatenação (junta)
    nome_completo: str = nome_inquilino +" "+ sobrenome_inquilino
    print(nome_completo)

    #Criar outra função para armazenar os dados do paciente
    #nome paciente
    #cidade natal
    #tipo sanguineo
    #idade => inteiro
    #peso =>real
    #altura =>

    #calcular o IMC
    #Calcular o ano de nascimento

    #apresentar tudo
    # Nomenclatura de uma função/método(def) deve sempre ser uma ação
    #exemplo: apresentar_dados_paciente

    #py main.py

def apresentar_dados_paciente():
    nome_paciente: str = "Ana"
    cidade_natal: str = "Blumenau"
    tipo_sanguineo: str = "AB+"
    idade: int = 20
    peso: int = 58
    altura: float = 1.68
    imc: int = peso / altura
    calcular_ano_nascimento: float = 2025 - idade

    apresentar_tudo: str = nome_paciente + " " + cidade_natal + " " + tipo_sanguineo + " " + str (idade) + " " + str (peso) + " " + str(altura) + " " + str(int(imc)) + " " + str(calcular_ano_nascimento)
    print(apresentar_tudo)

   # print("Nome:"+ nome_paciente)
   # print("Cidade Natal:" + cidade_natal)
   # print("Tipo Sanguíneo:" + tipo_sanguineo)

def exemplo_int_float():
    salario: int = 1500
    aumento: float = 1.30

    novo_salario: float = salario * aumento

    #str(novo_salario) => converter de float para string
    print("Novo salário: " + str(novo_salario))


def exemplo_boolean():
    #Boolean: True(verdadeiro) ou False(falso)
    empregado: bool = True
    
    #Alterando o valor da variável empregado
    empregado = False

    print("Empregado: " + str(empregado))
    
