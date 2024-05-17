from robot_dife_despl import despl
from robot_dife_giro import giro
from matrices import matrix




# Solicitar al usuario la entrada
#trayectoria_input = input("Ingrese las coordenadas como 'x,y; x,y; ...': ")
trayectoria_input = "0,5;5,5;5,0;0,0" #cuadrado
#trayectoria_input = "0,5;2.5,5;2.5,0;0,0" #rectangulo
#trayectoria_input = "-0.73,1;1.38,2.39;3.09,1.38;2.36,0;0,0" #pentagono
#trayectoria_input = "-1,1;0,2;5,2;6,1;5,0;0,0" #Figura rara


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

#Mientras mande un true funciona el programa pero si mando un fa

    #while True:  # Sub-bucle que actúa como pausa
        #respuesta = input("Ingrese 'True' para continuar: ")
        #if respuesta.strip().lower() == "true":  # Si recibe "True", sigue con el bucle principal
            #break  # Rompe el sub-bucle para volver al bucle principal
        #else:
            #print("Esperando la señal para continuar...")