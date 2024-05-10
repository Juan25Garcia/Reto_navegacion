from robot_dife_despl import despl
from robot_dife_giro import giro
from matrices import matrix


# Solicitar al usuario la entrada
trayectoria_input = input("Ingrese las coordenadas como 'x,y; x,y; ...': ")

# Llamar a la función para obtener vectores X e Y
xdir, ydir = matrix(trayectoria_input)

# Imprimir los vectores resultantes
print("Vector X:", xdir)
print("Vector Y:", ydir)

x_now = 0
y_now = 0
theta_now = 0
x_now, y_now, theta_now = giro(x_now, y_now, theta_now, xdir[0], ydir[0])
x_now, y_now, theta_now = despl(x_now, y_now, theta_now, xdir[0], ydir[0])
i =1

for i in range(len(xdir)-1):
    x_now, y_now, theta_now = giro(x_now, y_now, theta_now, xdir[i], ydir[i])
    while True:  # Sub-bucle que actúa como pausa
        respuesta = input("Ingrese 'True' para continuar: ")
        
        if respuesta.strip().lower() == "true":  # Si recibe "True", sigue con el bucle principal
            break  # Rompe el sub-bucle para volver al bucle principal
        else:
            print("Esperando la señal para continuar...")

    x_now, y_now, theta_now = despl(x_now, y_now, theta_now, xdir[i], ydir[i])
