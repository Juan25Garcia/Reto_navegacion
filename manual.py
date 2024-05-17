import numpy as np
import msvcrt
import matplotlib.pyplot as plt

# Configuración inicial del gráfico
fig, ax = plt.subplots()
carrito, = ax.plot(0, 0, 'ro')  # Representación del carrito como un punto rojo
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.ion()  # Hacer la gráfica interactiva
plt.show()

x = 0
y = 0
theta = 0  # Ángulo de orientación inicial en radianes

while True:
    if msvcrt.kbhit():  # Verifica si hay una tecla presionada
        direccion = msvcrt.getch()  # Lee una tecla presionada
        if direccion == b'w':
            print("Enfrente")
            x += np.cos(theta)
            y += np.sin(theta)
        elif direccion == b's':
            print("Atrás")
            x -= np.cos(theta)
            y -= np.sin(theta)
        elif direccion == b'a':
            print("Izquierda")
            theta += np.pi / 8  # Girar 22.5 grados a la izquierda
        elif direccion == b'd':
            print("Derecha")
            theta -= np.pi / 8  # Girar 22.5 grados a la derecha
        elif direccion == b' ':
            print("Cerrando")
            break

        # Graficación
        ax.cla()  # Limpiar el contenido del eje antes de actualizar
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.plot(x, y, 'ro')  # Actualizar la posición del carrito

        # Para visualizar la dirección con una línea verde
        ax.plot([x, x + 0.5 * np.cos(theta)], [y, y + 0.5 * np.sin(theta)], 'g-', linewidth=2)

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Simulación del Robot")
        plt.pause(0.0000001)  # Pausa breve para actualizar la gráfica

plt.ioff()
plt.show()
print("Programa finalizado.")
