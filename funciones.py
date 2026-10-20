
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

    
