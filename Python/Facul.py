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

total = 0

for cod, prdo in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(F"{prod[0]}: R$ {subtotal:.2f}")
    total += subtotal
print(20 * "_")
print(F"total: R$ {total:.2f}")

