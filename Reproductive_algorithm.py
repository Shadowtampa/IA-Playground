import os
from pynput import keyboard
# ---------------------------------------------------------------------------------------Importações-------------------------------------------------------------------------------------------------------------------------


def main():
    player = Player([0, 0])
    board = Board(player)

    board.render_board()

    entrada = ''
    while entrada != 'q':
        if (entrada == 'w'):
            player.move_up()
            board.render_board()
            
        if keyboard.on_press('s'):
            player.move_down()
            board.render_board()

        if (entrada == 'a'):
            player.move_left()
            board.render_board()
                     q
        if (entrada == 'd'):
            player.move_right()
            board.render_board()

# ---------------------------------------------------------------------------------------Utilização do main-------------------------------------------------------------------------------------------------------------------------


class Board:
    def __init__(self, player, dimensions=(5, 5)):
        self.shape = (dimensions[0], dimensions[1])  # linhas x coluna
        self.player_coords = player.get_dimensions()

    def render_board(self):
        if (self.player_coords[0] >= self.shape[0]-1):
            self.player_coords[0] = self.shape[0] - 1
        
        if (self.player_coords[1] >= self.shape[1]-1):
            self.player_coords[1] = self.shape[1] - 1
            
        if (self.player_coords[0] < 0):
            self.player_coords[0] = 0
            
        if (self.player_coords[1] < 0):
            self.player_coords[1] = 0
        
        os.system('cls')
        print('board coords',self.shape[0]-1,self.shape[1]-1)
        print('player coords',self.player_coords)
        print('Novo Tabuleiro')

        for i in range(self.shape[0]):
            if i == self.player_coords[0]:
                print(*[Chunk(False, (i, _)).render() if _ != self.player_coords[1]
                        else Player(self.player_coords).render() for _ in range(self.shape[1])])

            else:
                print(*[Chunk(False, (i, _)).render()
                        for _ in range(self.shape[1])])


class Square:
    def __init__(self, position, shape=''):
        self.shape = shape
        self.position = position
        # print('solid?', self.solid)

    def render(self):
        return self.shape

    def get_dimensions(self):
        return self.position


class Chunk(Square):
    def __init__(self, state, position):
        super().__init__(position, shape='')
        self.solid = state
        self.check_solidity()

    def check_solidity(self):
        if self.solid:
            self.shape = '[X]'
        else:
            self.shape = '[ ]'


class Player(Square):
    def __init__(self, position):
        super().__init__(position, shape='[P]')

    def move_up(self, steps=1):
        self.position[0] += -1

    def move_down(self, steps=1):
        self.position[0] += 1

    def move_left(self, steps=1):
        self.position[1] += -1

    def move_right(self, steps=1):
        self.position[1] += 1


# ---------------------------------------------------------------------------------------Definição de Classes-------------------------------------------------------------------------------------------------------------------------
main()
