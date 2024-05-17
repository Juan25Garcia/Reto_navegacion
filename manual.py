import msvcrt



def velocidades (direccion):
    x = 0
    y = 0
    if direccion == b'w':
        print("Enfrente")
        y+=1
        print(y)
    elif direccion ==b's':
        print("Atras")
        y-=1
        print(y)
    elif direccion ==b'a':
        print("Izquierda")
        print()
    elif direccion ==b'd':
        print("Derecha")
        print()
    elif direccion == b' ':
        print("Cerrando")


while True:
    direccion= msvcrt.getch()
    velocidades(direccion) 
    if direccion == b' ':
        break