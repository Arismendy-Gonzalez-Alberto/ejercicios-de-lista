# Pedir palabra y contar vocales
palabra = input("Introduce una palabra: ")

# Mostrar resultados
print(f"\nEn '{palabra}' hay:")
for vocal in 'aeiou':
    print(f"- {vocal}: {palabra.count(vocal)}")