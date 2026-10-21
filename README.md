# ⚓ Battleship (Hundir la Flota) in Python

A classic "Battleship" game developed entirely in Python to be played from the terminal. In this versi
on, the user plays against the machine on a 10x10 board.

## 🚀 Features
*   **Random Generation:** Both players' ships are placed randomly without colliding.
*   **Placement Intelligence:** The algorithm prevents ships from overlapping or touching.
*   **Parallel Visualization:** The terminal displays both boards (the player's fleet and the shooting board) side by side for a seamless gaming experience.

## 🛠️ Project Structure
The code is modularized following best programming practices:
*   `main.py`: Main script that runs the game loop and manages the turn-based system.
*   `clases.py`: Contains the core game logic using Object-Oriented Programming (the `Tablero` class).
*   `funciones.py`: Auxiliary functions handling the visual interface and printing of matrices.
*   `variables.py`: Stores the core game constants (board dimensions, ship inventory).

## 🎮 How to Play
1. Clone this repository:
   ```bash
   git clone [https://github.com/larasarasola2-maker/battleship-python.git](https://github.com/larasarasola2-maker/battleship-python.git)
   ```
2. Navigate to the project folder and run the main script:
   ```bash
   python main.py
   ```
3. Enter the (X, Y) coordinates when it is your turn. Try to sink the enemy fleet before the machine destroys yours!

## 👤 Author
*   **[Lara Sarasola]** - Ramp-Up Project (Data Science Bootcamp)

