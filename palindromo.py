
palabra = input("Introduce una palabra: ")

palabra_min = palabra.lower()

if palabra_min == palabra_min[::-1]:

    print(f'"{palabra}" es un palíndromo')
else:
    
    print(f'"{palabra}" no es un palíndromo')