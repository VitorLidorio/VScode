#troco
valor = int(input("Entre com 0 valor desejado do saque: "))

notas = (100, 50, 20, 10, 5)

notas100 = int(valor / notas[0])
valor = valor % notas[0]
print("Entregar", notas100, "Notas de", notas[0])
notas50 = int(valor / notas[1])
valor = valor % notas[1]
print("Entregar", notas50, "Notas de", notas[1])
notas20 = int(valor / notas[2])
valor = valor % notas[2]
print("Entregar", notas20, "Notas de", notas[2])
notas10 = int(valor / notas[3])
valor = valor % notas[3]
print("Entregar", notas10, "Notas de", notas[3])
notas5 = int(valor / notas[4])
valor = valor % notas[4]
print("Entregar", notas5, "Notas de", notas[4])
