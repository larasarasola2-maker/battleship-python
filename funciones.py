
def print_tablero(tablero):
    print("=====================================")
    for fila in tablero:
        # Convertimos cada elemento a texto y los unimos con un par de espacios
        fila_formateada = "  ".join(str(elemento) for elemento in fila)
        print(fila_formateada)
    print("=====================================")

def string_to_ints(string):
      '''Recibe un string del tipo "x1,y1" y devuelve dos variables ints x1, y1'''
      lista= string.split(sep=",")
      x1 = int(lista[0])
      y1 = int(lista[1])
      return x1, y1

def print_tableros_juntos(tablero_jugador, tablero_maquina):
    # Centramos los títulos (cada tablero ocupa unos 28 caracteres)
    titulo_izq = "TU TABLERO".center(28)
    titulo_der = "TABLERO MÁQUINA".center(28)
    
    print(f"{titulo_izq}   |   {titulo_der}")
    print("=============================   |   =============================")
    
    # zip() recorre la fila 0 de ambos a la vez, luego la 1, etc.
    for fila_izq, fila_der in zip(tablero_jugador, tablero_maquina):
        
        # Formateamos ambas filas igual que en la primera función
        str_izq = "  ".join(str(elemento) for elemento in fila_izq)
        str_der = "  ".join(str(elemento) for elemento in fila_der)
        
        # Las imprimimos juntas separadas por una barra
        print(f"{str_izq}   |   {str_der}")
        
    print("=============================   |   =============================")

def desanimar_animar(contador_m,contador_u,nombre):
    if contador_m > contador_u: #Desanimamos al jugador para que salga del juego
        if (contador_m == 2):
                pregunta = input("La máquina está en racha ¿Estás seguro que quieres seguir intentándolo? s/n")
                if pregunta == "s":
                    pass
                else: 
                    print("Has perdido, hasta la próxima :)")
                    print("Resultados: Máquina", contador_m, nombre,":", contador_u)
                    exit()
        elif (contador_m == 3):
                    pregunta = input("La máquina te está sacando mucha ventaja, ¿quieres seguir?  s/n")
                    if pregunta == "s":
                        pass
                    else:
                        print("Has perdido, hasta la próxima :)")
                        print("Resultados: Máquina", contador_m, nombre,":", contador_u) 
                        exit()
        
        elif (contador_m >= 4):
                        pregunta = input("No te quiero desanimar pero va a ser complicado remontar, ¿quieres seguir?  s/n")
                        if pregunta == "s":
                            pass
                        else: 
                            print("Has perdido, hasta la próxima :)")
                            print("Resultados: Máquina", contador_m, nombre,":", contador_u) 
                            exit()
        else:
            pass
    else: #Animamos pero incitamos a salir
        if (contador_u == 2):
            pregunta = input("Vas muy bien ¿seguimos? s/n")
            if pregunta == "s":
                pass
            else: 
                print("Has ganado!!!! Enhorabuenaaa, hasta la próxima :)")
                print("Resultados: Máquina", contador_m, nombre,":", contador_u)
                exit()
        elif (contador_u==3):
            pregunta = input("Está claro que vas a ganar ¿seguimos? s/n")
            if pregunta == "s":
                pass
            else: 
                print("Has ganado!!!! Enhorabuenaaa, hasta la próxima :)")
                print("Resultados: Máquina", contador_m, nombre,":", contador_u)
                exit()
        elif (contador_u>=4):
                    pregunta = input("¡Qué bueno eres al hundir la flota! La máquina ya no tiene nada que hacer ¿seguimos? s/n")
                    if pregunta == "s":
                        pass
                    else: 
                        print("Has ganado!!!! Enhorabuenaaa, hasta la próxima :)")
                        print("Resultados: Máquina", contador_m, nombre,":", contador_u)
                        exit()

