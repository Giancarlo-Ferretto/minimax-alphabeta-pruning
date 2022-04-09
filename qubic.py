from copy import copy, deepcopy

class State():
    def __init__(self, matrix, next_player = 'X', moves_count = 0, last_player = None, last_action = None):
        self.matrix = deepcopy(matrix)
        self.next_player = next_player
        self.last_player = last_player
        self.last_action = last_action
        self.moves_count = moves_count
        self.visited = False
        self.value = 0
        self.alpha = 0
        self.beta = 0
        self.parent = None
        self.children= []

    def get_actions(self):
        actions = []
        for x in range (4):
            for y in range (4):
                for z in range (4):
                    if self.matrix[x][y][z] == '-':
                        actions.append(Action(x, y, z))
        return actions

    def transition(self, action):
        self.matrix[action.x][action.y][action.z] = self.next_player
        self.last_player = self.next_player
        self.last_action = action
        if self.next_player == 'X': self.next_player = 'O'
        else: self.next_player = 'X'
        self.moves_count += 1

    def get_winner(self):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                if dx == 0 and dy == 0 and dz == 0:
                                    continue
                                try:
                                    if self.matrix[i][j][k] != '-' and self.matrix[i][j][k] == self.matrix[i+dx][j+dy][k+dz] and self.matrix[i][j][k] == self.matrix[i+2*dx][j+2*dy][k+2*dz] and self.matrix[i][j][k] == self.matrix[i+3*dx][j+3*dy][k+3*dz]:
                                        return self.matrix[i][j][k]
                                except:
                                    continue
        return None

    def __copy__(self):
        return type(self)(self.matrix, self.next_player, self.moves_count, self.last_player, self.last_action)

class Action():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

def alpha_beta_pruning(state):
    state = deepcopy(state)
    state.parent=None

    current_player = state.next_player
    stack = [state]
    
    iter_counter = 0
    while len(stack) > 0:
        s = stack[-1] # no se elimina del stack

        if s.visited == False: # primera visita
            s.visited = True

            #descarte de rama
            if s.parent is not None and s.parent.parent is not None:
                if current_player == s.next_player and s.parent.beta <= s.parent.parent.alpha: continue
                if current_player != s.next_player and s.parent.alpha >= s.parent.parent.beta: continue

            if s.get_winner() is not None: continue # final state

            iter_counter+=1

            actions = s.get_actions()

            for a in actions:
                child = copy(s) # no copia los hijos del nodo (copia valores de alpha y beta)
                child.alpha=s.alpha; child.beta=s.beta
                child.parent=s

                child.transition(a)
                stack.append(child)

                # se agrega el hijo a s
                s.children.append(child)

        else: # en la segunda visita calculamos el valor
            if len(s.children) == 0: #final state
            #en caso de ser estado final asignamos 
            #1 si gana el current_player, -1 si pierde y 0 si empatan
                winner = s.get_winner()
                s.value=0
                if current_player == winner:
                    s.value=1
                elif winner is not None:
                    s.value=-1

            else: #not final state
                # el valor se obtiene de los estados hijos
                if current_player == s.next_player:
                    s.value = max([ss.value for ss in s.children])
                else:
                    s.value = min([ss.value for ss in s.children])

            if current_player == s.next_player:
                if s.parent is not None and s.value < s.parent.beta: s.parent.beta=s.value
            else:
                if s.parent is not None and s.value > s.parent.alpha: s.parent.alpha=s.value
            stack.pop()
    #retorna la lista de acciones con sus valores asociados
    return [[ss.last_action, ss.value] for ss in state.children], iter_counter

# matriz[x][y][z]
# x plano
# y fila
# z columna 

matrix = [['-','-','-','-'],
          ['-','-','-','-'],
          ['-','-','-','-'],
          ['-','-','-','-']], [['-','-','-','-'],
                               ['-','-','-','-'],
                               ['-','-','-','-'],
                               ['-','-','-','-']], [['-','-','-','-'],
                                                    ['-','-','-','-'],
                                                    ['-','-','-','-'],
                                                    ['-','-','-','-']], [['-','-','-','-'],
                                                                         ['-','-','-','-'],
                                                                         ['-','-','-','-'],
                                                                         ['-','-','-','-']]

state = State(matrix, 'X', 0)

state.transition(Action(0, 0, 0))
state.transition(Action(0, 1, 0))
state.transition(Action(1, 1, 0))
state.transition(Action(0, 2, 0))
state.transition(Action(2, 2, 0))
state.transition(Action(0, 3, 0))
#state.transition(Action(3, 3, 0))

print("TABLERO:", state.matrix)

#winner = state.get_winner()

#if winner != None:
#    print("\nthe winner is", winner, "in", state.last_action)
#else: 
#    print("\nthe game is not over")

actions, iters = alpha_beta_pruning(state)

print("JUGADOR ACTUAL:", state.next_player)
print("ITERACIONES REALIZADAS:", iters)

for action in actions:
    print(action[0], action[1])