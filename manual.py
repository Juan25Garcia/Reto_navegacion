import numpy as np
import keyboard
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
    if keyboard.is_pressed('w'):
        x += np.cos(theta)
        y += np.sin(theta)
    elif keyboard.is_pressed('s'):
        x -= np.cos(theta)
        y -= np.sin(theta)
    elif keyboard.is_pressed('a'):
        theta += np.pi / 8  # Girar 22.5 grados a la izquierda
    elif keyboard.is_pressed('d'):
        theta -= np.pi / 8  # Girar 22.5 grados a la derecha
    elif keyboard.is_pressed(' '):
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
    plt.pause(0.01)  # Pausa breve para actualizar la gráfica

plt.ioff()
plt.show()
print("Programa finalizado.")
