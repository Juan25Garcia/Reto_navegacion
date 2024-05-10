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

    
for i in range(len(xdir)):
    x_now, y_now, theta_now = giro(x_now, y_now, theta_now, xdir[i], ydir[i])
    x_now, y_now, theta_now = despl(x_now, y_now, theta_now, xdir[i], ydir[i])
