import numpy as np

# Definir la función para separar coordenadas
def matrix(trayectoria_input):
    """
    Toma una cadena de coordenadas en formato "x,y; x,y; ..." y devuelve dos listas:
    una para valores en X y otra para valores en Y.
    """
    # Dividir la entrada en pares de coordenadas
    puntos = trayectoria_input.split(';')

    # Crear una lista para la matriz de trayectoria
    trayectoria = []

    # Convertir la lista de cadenas en una matriz de coordenadas
    for punto in puntos:
        # Eliminar espacios y dividir por coma
        x, y = map(float, punto.strip().split(','))
        trayectoria.append([x, y])

    # Convertir la lista a una matriz numpy
    trayectoria = np.array(trayectoria)

    # Extraer los vectores X e Y
    x_vals = trayectoria[:, 0]  # Todos los valores en la primera columna
    y_vals = trayectoria[:, 1]  # Todos los valores en la segunda columna

    return x_vals, y_vals  # Devolver los vectores separados

# Uso de la función
# Solicitar al usuario la entrada
#trayectoria_input = input("Ingrese las coordenadas como 'x,y; x,y; ...': ")

# Llamar a la función para obtener vectores X e Y
#x_vals, y_vals = matrix(trayectoria_input)

# Imprimir los vectores resultantes
#print("Vector X:", x_vals)
#print("Vector Y:", y_vals)
