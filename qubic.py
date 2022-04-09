from copy import deepcopy

class State():
    def __init__(self, matrix, next_player = 'X', moves_count = 0, last_player = None, last_action = None):
        self.matrix = deepcopy(matrix)
        self.next_player = next_player
        self.last_player = last_player
        self.last_action = last_action
        self.moves_count = moves_count

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
        if self.last_action is None: return None
        last_x = self.last_action.x
        last_y = self.last_action.y
        last_z = self.last_action.z
        print("last action", last_x, last_y, last_z)
        last_player = self.last_player
        print("last player", last_player)

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

class Action():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"


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
state.transition(Action(3, 3, 0))

winner = state.get_winner()

if winner != None:
    print("\nthe winner is", winner, "in", state.last_action)
else: 
    print("\nthe game is not over")
