# ⚓ Hundir la Flota (Battleship) en Python

Un juego clásico de "Hundir la Flota" desarrollado completamente en Python para jugarse desde la terminal. En esta versión, el usuario se enfrenta a la máquina en un tablero de 10x10.

## 🚀 Características
*   **Generación aleatoria:** Los barcos de ambos jugadores se colocan de forma aleatoria sin colisionar entre ellos.
*   **Inteligencia de colocación:** El algoritmo evita que los barcos se superpongan o se toquen.
*   **Visualización en paralelo:** La terminal muestra ambos tableros (el del jugador y el de disparos) alineados para una mejor experiencia de juego.

## 🛠️ Estructura del Proyecto
El código está modularizado siguiendo las mejores prácticas:
*   `main.py`: Archivo principal que ejecuta el bucle del juego y gestiona los turnos.
*   `clases.py`: Contiene la lógica principal del juego mediante Programación Orientada a Objetos (clase `Tablero`).
*   `funciones.py`: Funciones auxiliares para la interfaz visual y la impresión de matrices.
*   `variables.py`: Almacena las constantes del juego (dimensiones, inventario de barcos).

## 🎮 Cómo jugar
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/hundir-la-flota.git](https://github.com/larasarasola2-maker/battleship-python.git)