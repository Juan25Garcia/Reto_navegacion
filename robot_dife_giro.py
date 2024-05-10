import numpy as np
import matplotlib.pyplot as plt

def giro (x,y,theta,xd,yd):
    # Tiempos
    Tf = 10  # Tiempo final
    t = 0    # Tiempo inicial
    dt = 0.01  # Intervalos de tiempo

    # Parámetros del coche
    R = 0.12  # Radio de llanta
    L = 0.78  # Distancia entre llantas

    # Valores iniciales
    #x = 0  # Posición actual en X
    #y = 0  # Posición actual en Y
    #theta = 0  # Orientación actual del coche

    # Constantes Giro
    kpr = 5  # Constante P para Giro (rotate)

    # Velocidad Máxima
    vmax = 5  # Velocidad Máxima

    # Valores deseados
    #xd = 5  # Posición deseada en X
    #yd = 5  # Posición deseada en Y
    thetad = 0  # Orientación deseada
    i = 1  # Iterador

    # Variables que no afecta el while son: xd, yd
    while t < Tf:
        # Control de Orientación
        thetadir = np.arctan2(yd - y, xd - x)  # Ángulo de dirección hacia el objetivo
        thetae = thetadir - theta  # Error angular
        
        # Saturación de giro
        if thetae > np.pi:
            thetae -= 2 * np.pi
        if thetae < -np.pi:
            thetae += 2 * np.pi

        w = kpr * thetae  # Velocidad angular

        # Velocidades de llantas
        vd = (L * w) / (2 * R)
        vi = -vd  # Velocidad de la llanta izquierda (en sentido contrario)

        # Simulación
        theta += w * dt  # Actualiza la orientación
        
        # Saturación para mantener theta entre -pi y pi
        if theta > np.pi:
            theta -= 2 * np.pi
        if theta < -np.pi:
            theta += 2 * np.pi

        # Detener la simulación si el coche está correctamente orientado
        if vd > 0 and thetae <= 0.001:
            Tf = 0
        if vd < 0 and thetae >= -0.001:
            Tf = 0

        # Graficación
        plt.figure(1)
        plt.scatter(x, y, label='Posición actual', color='blue')
        plt.scatter(xd, yd, label='Posición deseada', color='red')
        plt.plot([x, x + 0.5 * np.cos(theta)], [y, y + 0.5 * np.sin(theta)], 'g-', linewidth=2)
        plt.axis([-10, 10, -10, 10])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Simulación del coche")
        plt.legend()
        plt.pause(0.01)  # Para ver los cambios durante la simulación
        plt.clf()  # Limpiar para el siguiente paso de simulación

        # Incrementar el iterador y el tiempo
        i += 1
        t += dt

    # Para evitar cerrar la ventana después de la simulación
    #plt.show()
    return x, y, theta 