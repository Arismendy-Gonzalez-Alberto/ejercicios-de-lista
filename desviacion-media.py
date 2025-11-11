entrada = input("Introduce números separados por comas: ")


numeros = [float(num) for num in entrada.split(',')]


media = sum(numeros) / len(numeros)

suma_diferencias = 0
for num in numeros:
    suma_diferencias += (num - media) ** 2
    
desviacion = (suma_diferencias / len(numeros)) ** 0.5


print(f"\nNúmeros: {numeros}")
print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")