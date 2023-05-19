produtos = {}

while True:
    print("Insira o código:")
    cod = int(input("Código: "))
    print("Insira o nome do produto")
    nome = input("Nome: ")
    print("Insira o preço do preduto:")
    preco = float(input("R$: "))
    print("Insira o Qtde:")
    qtde = int(input("Qtde: "))
    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    produtos.update({cod: prod})
    resp = input("Deseja continuar [S/N]? ")
    if resp == "N" or resp == "n":
        break
print("Código:", cod)
print("Nome do produto:", nome)
print("Preço: R$", preco)
print("Qtde:", qtde)


