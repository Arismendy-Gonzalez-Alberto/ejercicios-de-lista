vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]


producto_escalar = 0
for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i]


print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Producto escalar: {producto_escalar}")