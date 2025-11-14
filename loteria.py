Entrada = input("¿cuales son tus numeros de la loteria primitiva?(separados por espacios): ")


numeros = [int(num) for num in Entrada.split()]

if len(numeros) != 3:
    print("Error: Debes ingresar exactamente 3 numeros.")
    exit()

numeros.sort()

print("Tus numeros de la loteria primitiva son(ordenados de menor a mayor): ")
print(numeros)