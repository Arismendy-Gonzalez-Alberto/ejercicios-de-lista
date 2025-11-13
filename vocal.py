palabra = input("Introduce una palabra: ")


vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1


print(f"\nEn la palabra '{palabra}' hay:")

for vocal, cantidad in vocales.items():
    
    print(f"- {vocal}: {cantidad}")