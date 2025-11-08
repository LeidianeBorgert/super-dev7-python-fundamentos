from questionary import select,checkbox
from datetime import datetime



def exercicios_dados_produtos():
    nome_produto: str = input("Digite o nome do produto: ")
    quantidade: int = int(input("Digite a quantidade: "))
    categorias_produtos = ["Esportes","Roupas Esportivas","Calçados","Acessórios","Equipamentos","Suplementos e Nutrição","Marcas","Ofertas e Categorias Especiais"]
    categoria_escolhida: str = select("Informe a categoria do produto: ", choices=categorias_produtos).ask()
    preco: float = float(input("Digite o preço: "))
    valor_total: float = quantidade * preco
    data: str = input("Insira a data de vencimento do produto: DD/MM/AAAA: " )
    formato = '%d/%m/%Y'
    data_vencimento = datetime.strptime(data,formato).date()
    data_atual = datetime.today().date()


    desconto_categorias = 0
    if categoria_escolhida == "Esportes":
        desconto_categorias = 0.10    
    elif categoria_escolhida == "Roupas Esportivas":
        desconto_categorias = 0.15
    elif categoria_escolhida == "Calçados":
        desconto_categorias = 0.20
    elif categoria_escolhida == "Acessórios":
        desconto_categorias = 0.12
    elif categoria_escolhida == "Equipamentos":
        desconto_categorias = 0.08
    elif categoria_escolhida == "Suplementos e Nutrição":
        desconto_categorias = 0.05
    elif categoria_escolhida == "Marcas":
        desconto_categorias = 0.07
    elif categoria_escolhida == "Ofertas e Categorias Especiais":
        desconto_categorias = 0.25

    desconto_percentural = valor_total * desconto_categorias
    desconto_aplicado = valor_total - desconto_percentural 

    if data_vencimento >= data_atual:
        desconto_data =  20 - desconto_aplicado
    elif data_vencimento == data_atual:
        desconto_data = 0.70 + desconto_categorias
    else:
        print("Produto vencido! Compra não permitida.")

    print("\nNome do produto: " + nome_produto)
    print( "Quantidade: " + str(quantidade))
    print("Preço unitário: " + str(preco) )
    print( "Categoria do Produto: " + categoria_escolhida)
    print("Percentual de desconto por categoria: " + str(desconto_categorias) + "%")
    print("Valor do desconto: " + str(desconto_percentural))
    print("Total da compra sem desconto : " + str(valor_total))
    print("Total da compra com desconto : " + str(desconto_aplicado))
    print("Data de vencimento do produto: " + str(data_vencimento))
    print("Desconto por data de vencimento do produto: " + str(desconto_data))

   


 






