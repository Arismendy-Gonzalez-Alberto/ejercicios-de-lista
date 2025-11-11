
abecedario = list("abcdefghijklmnopqrstuvwxyz")


for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:  
        abecedario.pop(i)


print("Abecedario sin las letras en posiciones múltiplos de 3:")
print(abecedario)