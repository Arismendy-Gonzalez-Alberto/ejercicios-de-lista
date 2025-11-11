materias = ["Matemáticas", "Física", "Química", "Biología", "Historia", "Lengua"]

notas = []

for materia in materias:
    while True:
            nota = float(input(f"Introduce la calificación para {materia} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            elif nota < 0 or nota > 10:
                print("La calificación debe estar entre 0 y 10. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Por favor, introduce un número.")

print("\nCalificaciones ingresadas:\n")

for i in range(len(notas)):
        print(f"mi Calificación en la materia de {materias[i]} es: {notas[i]}")