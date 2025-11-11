Entrada = input("¿cuales son tus numeros de la loteria primitiva?(separados por espacios): ")

numeros = [int(num) for num in Entrada.split()]

numeros.sort()

print("Tus numeros de la loteria primitiva son(ordenados de menor a mayor): ")
print(numeros)