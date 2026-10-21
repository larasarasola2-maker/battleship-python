# Valores constantes en todas las partidas

#COSTANTES TABLERO-------------------------
#Tamaño tablero
dim_x =10
dim_y =10

#Creamos un tablero vacío (lista de listas)
coord_tab = []
for i in range (0,dim_x):
    fila = []
    for j in range (0,dim_y):
        fila.append(0)
    coord_tab.append(fila)


#BARCOS----------------------------------------
#Barcos (numero posiciones que ocupa : numero barcos)
dic_barcos = {1 : 4, 2 : 3, 3 : 2, 4 : 1}

#JUGADORES--------------------------------------
nombre2 = "Máquina"

#FEEDBACK----------------------------------------
mensaje_emitido = {
    'm_2': False, # Máquina llega a 2
    'm_3': False, # Máquina llega a 3
    'm_4': False, # Máquina llega a 4
    'u_2': False, # Usuario llega a 2
    'u_3': False, # Usuario llega a 3
    'u_4': False  # Usuario llega a 4
}

