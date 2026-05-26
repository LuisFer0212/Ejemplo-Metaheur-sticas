import random

# Este es el límite que no puede superar el rectángulo.
perimetro_maximo = 100

# Se crea una solución inicial aleatoria.
# El largo y el ancho empiezan con valores entre 1 y 40.
largo = random.randint(1, 40)
ancho = random.randint(1, 40)

# Se revisa si la solución inicial cumple con el perímetro.
# Si no cumple, se vuelve a generar otra solución.
while 2 * (largo + ancho) > perimetro_maximo:
    largo = random.randint(1, 40)
    ancho = random.randint(1, 40)

# Esta variable indica si el algoritmo todavía encontró una mejora.
mejora = True

# Esta variable solo sirve para contar las iteraciones.
iteracion = 1

print("Hill Climbing - Maximización del área de un rectángulo")
print("------------------------------------------------------")

print("Solución inicial:")
print("Largo:", largo)
print("Ancho:", ancho)
print("Área:", largo * ancho)
print("Perímetro:", 2 * (largo + ancho))
print()

# El ciclo se mantiene mientras el algoritmo siga mejorando.
while mejora:

    # Al inicio de cada vuelta se asume que no hay mejora.
    mejora = False

    # Se calcula el área de la solución actual.
    area_actual = largo * ancho

    # Se crean soluciones vecinas.
    # Un vecino es un pequeño cambio en el largo o en el ancho.
    vecinos = [
        (largo + 1, ancho),       # Aumenta el largo.
        (largo - 1, ancho),       # Disminuye el largo.
        (largo, ancho + 1),       # Aumenta el ancho.
        (largo, ancho - 1),       # Disminuye el ancho.
        (largo + 1, ancho - 1),   # Cambia largo y ancho.
        (largo - 1, ancho + 1)    # Cambia largo y ancho al revés.
    ]

    # Se revisan todos los vecinos generados.
    for nuevo_largo, nuevo_ancho in vecinos:

        # Se descartan dimensiones negativas o iguales a cero.
        if nuevo_largo <= 0 or nuevo_ancho <= 0:
            continue

        # Se calcula el perímetro del vecino.
        nuevo_perimetro = 2 * (nuevo_largo + nuevo_ancho)

        # Se revisa que el vecino no supere el perímetro máximo.
        if nuevo_perimetro <= perimetro_maximo:

            # Se calcula el área del vecino.
            nueva_area = nuevo_largo * nuevo_ancho

            # Si el vecino tiene mayor área, se acepta como nueva solución.
            if nueva_area > area_actual:
                largo = nuevo_largo
                ancho = nuevo_ancho

                # Se marca que sí hubo una mejora.
                mejora = True

                # Se sale del for para empezar otra iteración desde la nueva solución.
                break

    # Se muestra el resultado de esta iteración.
    print("Iteración", iteracion)
    print("Largo:", largo)
    print("Ancho:", ancho)
    print("Área:", largo * ancho)
    print("Perímetro:", 2 * (largo + ancho))
    print()

    # Se aumenta el contador de iteraciones.
    iteracion += 1

# Cuando ya no hay mejora, el algoritmo termina.
print("Mejor solución encontrada")
print("-------------------------")
print("Largo:", largo)
print("Ancho:", ancho)
print("Área máxima encontrada:", largo * ancho)
print("Perímetro utilizado:", 2 * (largo + ancho))
print("Perímetro máximo permitido:", perimetro_maximo)