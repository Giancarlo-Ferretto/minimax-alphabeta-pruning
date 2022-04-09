# Qubic Game (Tic-Tac-Toe 3D)

Es la evolución perversa del clásico tres en raya, pero en el Qubic debes conseguir cuatro figuras en línea para ganar y es en tres dimensiones. El tablero también es un poco diferente, ya que tiene cuatro planos de 4x4 en un universo de tres dimensiones, por lo cuál conseguir cuatro figuras horizontales, verticales, sobre planos o através de los planos es un poco más difícil ya que hay un número mayor de combinaciones ganadoras posibles. Siendo un juego de estrategia abstracta para dos jugadores.

![image](https://user-images.githubusercontent.com/81869512/162595041-479004ae-3139-4458-81a3-73a08216f457.png)

En el tablero 4x4x4 existen 76 combinaciones ganadoras posibles. En cada uno de los planos 4x4 hay cuatro columnas, cuatro filas y dos diagonales ganadoras, lo que ya suma 40 combinaciones ganadoras. También hay 16 líneas verticales que atraviesan los planos, ocho planos verticales que suman dos diagonales posibles y finalmente dos planos verticales que involucran diagonales de los planos 4x4 que suman otras diagonales más y esquinas y celdas posibles.

Claramente la estrategia para ganar el Tic-Tac-Toe 3D es demasiado complicada y extensa para ser aplicada por jugadores humanos, pero no imposible.

# Minimax


# Poda alpha beta
```
TABLERO: 
['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']
['O', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']

SIGUIENTE JUGADOR: X

ITERACIONES REALIZADAS PARA ENCONTRAR LA ACCIÓN GANADORA DEL JUGADOR 'X': 58
[[0, 0, 1] 0], [[0, 0, 2] 0], [[0, 0, 3] 0], [[0, 1, 1] 0], [[0, 1, 2] 0], 
[[0, 1, 3] 0], [[0, 2, 1] 0], [[0, 2, 2] 0], [[0, 2, 3] 0], [[0, 3, 1] 0], 
[[0, 3, 2] 0], [[0, 3, 3] 0], [[1, 0, 0] 0], [[1, 0, 1] 0], [[1, 0, 2] 0], 
[[1, 0, 3] 0], [[1, 1, 1] 0], [[1, 1, 2] 0], [[1, 1, 3] 0], [[1, 2, 0] 0], 
[[1, 2, 1] 0], [[1, 2, 2] 0], [[1, 2, 3] 0], [[1, 3, 0] 0], [[1, 3, 1] 0], 
[[1, 3, 2] 0], [[1, 3, 3] 0], [[2, 0, 0] 0], [[2, 0, 1] 0], [[2, 0, 2] 0], 
[[2, 0, 3] 0], [[2, 1, 0] 0], [[2, 1, 1] 0], [[2, 1, 2] 0], [[2, 1, 3] 0], 
[[2, 2, 1] 0], [[2, 2, 2] 0], [[2, 2, 3] 0], [[2, 3, 0] 0], [[2, 3, 1] 0], 
[[2, 3, 2] 0], [[2, 3, 3] 0], [[3, 0, 0] 0], [[3, 0, 1] 0], [[3, 0, 2] 0], 
[[3, 0, 3] 0], [[3, 1, 0] 0], [[3, 1, 1] 0], [[3, 1, 2] 0], [[3, 1, 3] 0], 
[[3, 2, 0] 0], [[3, 2, 1] 0], [[3, 2, 2] 0], [[3, 2, 3] 0], [[3, 3, 0] 1], 
[[3, 3, 1] 0], [[3, 3, 2] 0], [[3, 3, 3] 0], 

ACCIÓN GANADORA PARA EL JUGADOR 'X': [[3, 3, 0] 1]

[Done] exited with code=0 in 1.159 seconds
```
