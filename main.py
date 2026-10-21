import variables
from clases import Tablero
import random
import funciones
import time


#Mensaje de bienvenida
print("Bienvenido/a a hundir la flota")
name1 = input("Escriba su nombre: ") 
#Creamos partida
partida = Tablero(name1)

for tab in [partida.tablero1,partida.tablero2]:
    #Generamos coordenadas de los barcos
    #No hace falta (el método colocar_barcos_tablero() ya llama a coord_aleatorias_barcos())
    #Colocamos barcos en el tablero
    partida.colocar_barcos_tablero(tab)

turno_jugador = True
contador_rondas = 0

while True:
    contador_rondas = contador_rondas + 1
    if turno_jugador:
        print("Tu turno")
        time.sleep(2)

        #DEMO------------------------------------------------ QUITAR LUEGO
        print("CHULETA TABLERO ENEMIGO")
        funciones.print_tablero(partida.tablero2)
        print("\n\n\n\n\n\n\n\n\n")
        #----------------------------------------------------


        #Para que queden alineados uso la función print_tableros_juntos
        funciones.print_tableros_juntos(partida.tablero1, partida.tablero_disparos)
        
        x1,y1 = funciones.string_to_ints(input("Introduce las coordenadas a las que quieres disparar con el formato x,y "))
    
        # Disparo
        resultado = partida.disparo(x1, y1, partida.tablero2, partida.tablero_disparos)
        if resultado == True:
            # Si aciertas (o repites casilla), sigue siendo tu turno. No hacemos nada.
            pass
        else:
            # Si fallas, cambia el turno a la máquina
            turno_jugador = False
            
            
    else:
        print("Le toca a la máquina")
        time.sleep(2)
        # Turno de la máquina
        #Para que dipare la máquina usamos disparo de la clase tablero pero pasándole números aleatorios
        #Seleccionamos dos enteros aleatorios
        x2 = random.randint(0,variables.dim_x-1)
        y2 = random.randint(0,variables.dim_y-1)

        # Disparo
        resultado = partida.disparo(x2, y2, partida.tablero1, partida.tablero1)

        if resultado == True:
            # Si acierta (o repite casilla), sigue siendo el turno de la máquina. No hacemos nada.
            pass
        else:
            # Si falla, cambia el turno al jugador
            turno_jugador = True

    if partida.gana_persona() or partida.gana_maquina():
        exit()

    contador_m = partida.contador_aciertos(partida.tablero1)
    contador_jugador = partida.contador_aciertos(partida.tablero_disparos)

    
    funciones.desanimar_animar(contador_m, contador_jugador, partida.nombre1, variables.mensaje_emitido)

    
    