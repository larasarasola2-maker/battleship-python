import variables
import random
import copy

class Tablero:
    
    #Variables fijas
    dim_x = variables.dim_x
    dim_y = variables.dim_y
    barcos = variables.dic_barcos
    nombre2 = variables.nombre2

    def __init__(self, nombre1):
        '''
        Atributos propios de cada partida los hacemos con costructor init:
        nombre1: string
        '''
        self.nombre1 = nombre1
        #Inicializamos los tableros vacíos, usamos deep copy para que no se sobreescriba el mismo tablero
        #Deep copy nos permite hacer copias de matrices.
        self.tablero1 = copy.deepcopy(variables.coord_tab) #Tablero jugador
        self.tablero2 = copy.deepcopy(variables.coord_tab) #Tablero máquina
        self.tablero_disparos = copy.deepcopy(variables.coord_tab)

    def coord_aleatorias_barcos(self):
        '''Método para inicializar el tablero asignando posiciones aleatorias a los barcos,
        devuelve una lista con tuplas formadas por las posiciones max y min de cada barco
        [(x1,x2,y1,y2),........] (cada tupla pertenece a un barco)'''
        
        lista_salida = []
        casillas_ocupadas = []

        #Colocamos barco por barco
        for clave, valor in self.barcos.items():
            
            dim_barco = clave
            contador_barcos = 0
            while contador_barcos < valor:
                #La orientacion puede ser N/S/E/O (1,2,3,4)
                orientacion = random.randint(1,4)
                #Necesito dos puntos para hacer una recta :)
                #Primer punto (pos_x1,pos_y1)
                pos_x1 = random.randint(0,9)
                pos_y1 = random.randint(0,9)

                if orientacion == 1:
                    pos_x2 = pos_x1
                    pos_y2 = pos_y1 + (dim_barco - 1)
                    
                elif orientacion == 2:
                    pos_x2 = pos_x1
                    pos_y2 = pos_y1 - (dim_barco - 1)

                elif orientacion == 3:
                    pos_x2 = pos_x1 + (dim_barco - 1)
                    pos_y2 = pos_y1

                elif orientacion == 4:
                    pos_x2 = pos_x1 - (dim_barco - 1)
                    pos_y2 = pos_y1 


                #Comprobamos si las posiciones máximas se salen del tablero
                if ((0<=pos_x2<= 9) and (0<=pos_y2<=9)):
                    #Generamos todas las casillas que ocupa este barco
                    casillas_barco_actual = []
                    for i in range(min(pos_x1, pos_x2), max(pos_x1, pos_x2) + 1):
                        for j in range(min(pos_y1, pos_y2), max(pos_y1, pos_y2) + 1):
                            casillas_barco_actual.append((i,j))

                    #Comprobamos si alguna de las casillas esta ya ocupada
                    hay_colision = False
                    #Comprobamos si hay un barco al lado
                    hay_barco_contiguo = False
                    for casilla in casillas_barco_actual:
                        # Por esto es importante que casillas_ocupadas sea una lista de tuplas
                        if casilla in casillas_ocupadas:
                            hay_colision = True
                            break

                        x_c, y_c = casilla
                        casillas_alrededor = [(x_c+1, y_c), (x_c-1, y_c), (x_c, y_c+1), (x_c, y_c-1)]
                        # Comprobamos si alguna de las casillas de alrededor ya está ocupada
                        for elemento in casillas_alrededor:
                            if elemento in casillas_ocupadas:
                                hay_barco_contiguo = True
                                break # Rompe este bucle 
                                
                        # Si hay barco contiguo salimos del primer for
                        if hay_barco_contiguo:
                            break
                        
                    if (not hay_colision) and (not hay_barco_contiguo):
                        #Guardo las posiciones ocupadas en la lista de casillas ocupadas
                        #IMPORTANTE: usar extend para que introduzca las coordenadas como tupla, para luego acceder a ellas en el bucle casilla
                            #Comportamiento extend: [(0,0), (0,1), (4,4), (4,5)]
                            #Comportamiento append: [ [(0,0), (0,1)], [(4,4), (4,5)] ]
                        casillas_ocupadas.extend(casillas_barco_actual)
                        #Guardo las posiciones en una lista de tuplas de la forma (x1,x2,y1,y2)
                        #IMPORTANTE usar append para introducir la tupla entera como un único bloque
                            #Comportamiento append: [(1, 4, 2, 2), (5, 5, 6, 8)]
                            #Comportamiento extend: [1, 4, 2, 2, 5, 5, 6, 8]
                        lista_salida.append((pos_x1,pos_x2,pos_y1,pos_y2))

                        #Si se cumplen las condiciones anteriores ya tenemos un barco válido    
                        contador_barcos = contador_barcos + 1       
          
                    #Si hay colision el pasa a la siguiente iteración del while
        return lista_salida

    def colocar_barcos_tablero(self,tablero):
        '''Con la función anterior ya sabemos las posiciones máximas y mínimas de los barcos
        ahora vamos a sustituir en el tablero los 0 por 1 en todos los puntos donde haya barco'''

        for elemento in self.coord_aleatorias_barcos():
            #Desempaquetamos la tupla para que sea más fácil de leer
            x1, x2, y1, y2 = elemento
            #Como dependiendo de la orientación x2 puede ser menor que x1 etc usamos max y min de esos valores
            #Lo mismo con y1,y2
            for i in range (min(x1,x2), max(x1,x2)+1):
                for j in range (min(y1,y2), max(y1,y2)+1):
                    tablero[i][j] = 1

        return tablero    

    def disparo(self,x,y, tablero_analizar, tablero_output):
        '''Le pasamos las coordenadas y si había un barco (en el tablero del oponente)
        en la posición que le hemos pasado ponemos una B (de barco) en el tablero de disparos 
        y si no había barco sustituímos ponemos una A (agua)'''

        '''Le paso también el tablero para que pueda disparar yo a la máquina
        (el tablero que analiza es tablero2) y para que la máquina me pueda dispara a mí
        (el tablero que analiza es tablero1)'''

        "Si disparo yo a la máquina tablero output es tablero_disparos"
        "Si la máquina me dispara a mí tablero output es mi tablero1"

        "La funcion devuelve True si hemos acertado con el disparo y false si fallamos"

        if (x<0) or (x>9) or (y>9) or (y<0):
            print("Alguna de las coordenadas que introduciste se sale del tablero, vuelva a intentarlo")
            return True
        elif tablero_analizar[x][y] == 1:
            tablero_output[x][y] = "B"
            tablero_analizar[x][y] = "B"
            print("Acierto")
            return True
        elif tablero_analizar[x][y] == 0:
            tablero_output[x][y] = "A"
            tablero_analizar[x][y] = "A"
            print("Fallo")
            return False
        else:
            print("Ya has disparado a esa casilla, vuelve a intentarlo")
            return True

    def contador_aciertos(self, tablero_output):
        '''Contamos los aciertos recorriendo el tablero y viendo cuantas casillas están 
        marcadas con B'''
        contador = 0
        for fila in tablero_output:
            for elemento in fila:
                if elemento == "B":
                    contador = contador + 1
        return contador

    def gana_persona(self):
        if self.contador_aciertos(self.tablero_disparos) == sum(variables.dic_barcos.values()):
            print("Has ganado")
            return True

    def gana_maquina(self):
        if self.contador_aciertos(self.tablero1) == sum(variables.dic_barcos.values()):
            print("Has perdido, gana la máquina")
            return True

    
        







