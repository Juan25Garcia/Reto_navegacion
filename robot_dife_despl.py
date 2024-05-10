import numpy as np
import matplotlib.pyplot as plt
import time 

def despl(x,y,theta,xd,yd):
    # Tiempos
    Tf = 10  # Tiempo final 
    t = 0    # Tiempo inicial 
    dt = 0.01  # Intervalos de tiempo

    # Parámetros del robot
    L = 0.78  # Distancia entre ruedas
    R = 0.12  # Radio de las ruedas

    # Constantes de control
    kpr = 1  # Constante P para giro
    kpt = 8  # Constante P para desplazamiento

    # Velocidad máxima
    vmax = 5  # Velocidad máxima

    # Posiciones iniciales y orientación
    #x = 0  # Posición inicial en X
    #y = 0  # Posición inicial en Y
    #theta = 0  # Orientación inicial


    # Posición deseada
    #xd = 5  # Posición deseada en X
    #yd = 5  # Posición deseada en Y

    # Almacenamiento de trayectoria
    x_trajectory = []
    y_trajectory = []

    # Bucle de simulación
    while t < Tf:
        # Control de orientación
        thetadir = np.arctan2(yd - y, xd - x)  # Dirección deseada
        thetae = thetadir - theta

        # Saturación de giro 
        if thetae > np.pi:
            thetae -= 2 * np.pi
        if thetae < -np.pi:
            thetae += 2 * np.pi

        # Velocidad angular
        w = kpr * thetae

        # Control de dirección
        d = np.sqrt((xd - x) ** 2 + (yd - y) ** 2)  # Distancia entre puntos
        v = kpt * d  # Velocidad lineal

        # Saturación de velocidad máxima
        if v > vmax:
            v = vmax

        # Simulación
        # Actualización de la orientación
        theta += w * dt

        # Saturación para mantener theta entre -pi y pi
        if theta > np.pi:
            theta -= 2 * np.pi
        if theta < -np.pi:
            theta += 2 * np.pi

        # Avance en la dirección actual
        xp = v * np.cos(theta)  # Velocidad en X
        yp = v * np.sin(theta)  # Velocidad en Y
        
        # Actualización de posición
        x += xp * dt
        y += yp * dt
        
        # Almacenamiento de posiciones para la trayectoria
        x_trajectory.append(x)
        y_trajectory.append(y)

        # Velocidades de llantas
        vi = (2 * ((2 * v) - (2 * w * L))) / R  # Velocidad llanta izquierda
        vd = vi + (L * w / R)  # Velocidad llanta derecha

        # Detener si está cerca del objetivo
        if d <= 0.01:
            Tf = 0

        # Graficación
        plt.figure(1)
        plt.plot(x_trajectory, y_trajectory, 'b-', label='Trayectoria')  # Trayectoria
        plt.scatter(x, y, color='red', label='Posición actual')  # Posición actual
        plt.scatter(xd, yd, color='green', label='Posición deseada')  # Posición deseada
        plt.plot([x, x + 0.5 * np.cos(theta)], [y, y + 0.5 * np.sin(theta)], 'k-', linewidth=2, label='Orientación')  # Orientación actual
        plt.axis([-10, 10, -10, 10])
        plt.xlabel('Posición X')
        plt.ylabel('Posición Y')
        plt.title('Simulación de movimiento del robot')
        plt.legend()
        plt.pause(0.01)  # Para ver la simulación en tiempo real
        plt.clf()  # Limpiar para la siguiente iteración

        # Actualizar el tiempo
        t += dt

    # Para ver el resultado final sin cerrar la ventana
    #plt.show()
    return x, y, theta 
