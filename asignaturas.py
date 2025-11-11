
materias = ["Matemáticas", "Física", " Química", "Historia", "Lengua"]


for i in range(len(materias) - 1, -1, -1):
    nota = float(input(f"¿Qué nota has sacado en {materias[i]}? "))
    

    if nota >= 5:
        materias.pop(i)

if materias:
    print("\nTienes que repetir las siguientes materias:")
    for materias in materias:
        print(f"- {materias}")
else:
    print("\n¡Enhorabuena! Has aprobado todas las materias.")