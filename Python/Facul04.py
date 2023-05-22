#facul
i = 0
soma = 0 
contagem = 0 
maior = 0 
menor = 1000000000
while i != -1:
    x = float(input("Digite algum número, para encerrar digite -1 "))
    if x != -1:
        soma = soma + x
        contagem += -1
        media= soma/contagem
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    else:
        i = -1
print("A soma total foi", soma)
print("A média geral dos números digitados foi", media)
print("O maior digitado foi", maior)
print("O menor digitado foi", menor)

