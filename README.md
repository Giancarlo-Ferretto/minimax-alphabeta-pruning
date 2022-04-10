# Qubic Game (Tic-Tac-Toe 3D)

Es la evolución perversa del clásico tres en raya, pero en el Qubic debes conseguir cuatro figuras en línea para ganar y es en tres dimensiones. El tablero también es un poco diferente, ya que tiene cuatro planos de 4x4 en un universo de tres dimensiones, por lo cuál conseguir cuatro figuras horizontales, verticales, sobre planos o através de los planos es un poco más difícil ya que hay un número mayor de combinaciones ganadoras posibles. Siendo un juego de estrategia abstracta para dos jugadores.

![image](https://user-images.githubusercontent.com/81869512/162595041-479004ae-3139-4458-81a3-73a08216f457.png)

En el tablero 4x4x4 existen 76 combinaciones ganadoras posibles. En cada uno de los planos 4x4 hay cuatro columnas, cuatro filas y dos diagonales ganadoras, lo que ya suma 40 combinaciones ganadoras. También hay 16 líneas verticales que atraviesan los planos, ocho planos verticales que suman dos diagonales posibles y finalmente dos planos verticales que involucran diagonales de los planos 4x4 que suman otras diagonales más y esquinas y celdas posibles.

Claramente la estrategia para ganar el Tic-Tac-Toe 3D es demasiado complicada y extensa para ser aplicada por jugadores humanos, pero no imposible.

# Modelo
***
## State()

El estado de este problema consiste en una matriz 4x4x4, es decir 4 niveles y en cada nivel 16 casillas.
Se inicializa la matriz vacía, en donde todas las casillas estarán con el símbolo '-'. Si un jugador realiza una acción entonces se cambiará por el símbolo 'X' o 'O' respectivamente.
Al momento de inicializar el estado, se recibirán los movimientos de los jugadores, un contador de movimientos y la última acción realizada. 
Dentro de la estructura del estado existirán variables que serán necesarias para que el algoritmo Alpha-beta pruning funcione correctamente, esto son : alpha, beta, parent y children. 

### get_actions()

Para obtener las acciones será necesario recorrer la matriz completamente. Si una casilla está vacía ('-'), su posición se almacenará en un arreglo llamado "actions". Estas acciones posibles se irán almacenando una a una hasta que no existan más, y finalmente se retornarán en el arreglo. 

### transition()

En esta función se pasará de un estado a otro. Para lograrlo se recibirá el estado actual y la acción a realizar, se marcará la casilla con 'O' o 'X' dependiendo a que jugador le toque. También se incrementará en uno el contador de movimientos.

### get_winner()

Basado en un algoritmo de java se implementó la función para obtener un ganador. Muy distinto a como se obtiene un ganador en un tic-tac-toe tradicional, esta función deberá buscar en un nivel adicional como si de un cubo 3D se tratara. Se analizarán cuatro coincidencias seguidas del símbolo 'O' o 'X', esto es, primero se buscará en 2D por cada capa si existe una línea horizontal, vertical o diagonal que cumpla (como un tic-tac-toe tradicional). Luego se buscará en 3D, es decir, si existe una línea que atraviese desde el primer piso hasta el último. Estas transversales pueden ser bien perpendiculares o escalonadas, lo importante es saber que tienen que atravesar los 4 pisos sin ser interrumpidas.
Finalmente se obtendrá el ganador, siendo el primer jugador que logre realizar una línea correctamente.

## Action()

```

class Action():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

```
¿Qué significa una acción? Simplemente marcar una casilla, es indicar en que posición se quiere jugar.
Se recibe la fila (x), columna (y) y la profundidad (z) de una determinada casilla y se guarda.

***

# Algoritmo Minimax
Resultados obtenidos por medio de la función `iterative_minimax(state)`:
```
TABLERO: 
['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']
['O', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']

SIGUIENTE JUGADOR: X

POSIBLES ACCIONES JUGADOR X: ??? (no hay resultados)
ITERACIONES REALIZADAS PARA ENCONTRAR LA ACCIÓN GANADORA DEL JUGADOR 'X': 13

ACCIÓN GANADORA PARA EL JUGADOR 'X': ??? (no hay resultados)

[Done] exited with code=0 in 600.078 seconds
```
No se obtuvieron resultados a partir de la función iterative_minimax en seiscientos segundos. Los logs nos indican que se realizaron más de miles de iteraciones entre diferentes acciones y estados posibles pero debido al gran tiempo de procesamiento y complejidad del algoritmo al revisar todas las ramas posibles del árbol, este no logra entregar resultados en un tiempo óptimo. Por esto se prefiere acortar ramas e implementar el algoritmo de poda alpha beta, según la evaluación de ramas y nodos.

# Algoritmo Alpha-Beta-Pruning
Resultados obtenidos por medio de la función `alpha_beta_pruning(state)`:
```
TABLERO: 
['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']
['O', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['X', '-', '-', '-'] ['-', '-', '-', '-'] 
['O', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-'] ['-', '-', '-', '-']

SIGUIENTE JUGADOR: X

POSIBLES ACCIONES JUGADOR X:
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
ITERACIONES REALIZADAS PARA ENCONTRAR LA ACCIÓN GANADORA DEL JUGADOR 'X': 58

ACCIÓN GANADORA PARA EL JUGADOR 'X': [[3, 3, 0] 1]

[Done] exited with code=0 in 1.159 seconds
```
