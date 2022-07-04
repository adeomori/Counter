from typing import Optional
import numpy as np
from scipy.ndimage import convolve1d, convolve
from typing import Optional

class Field:
    def __init__(self, height: int, width: int, num_players: int) -> None:
        self.height = height
        self.width = width
        self.num_players = num_players
        self.field = -np.ones((self.height, self.width))
    
    def turn(self, column: int, player: int) -> int:
        if column > self.width or column < 0:
            # column out of bounds
            return 1
        else:
            if self.field[0, column] != -1:
                # column is full
                return 2
            else:
                if self.field[self.height - 1, column] == -1:
                    row = self.height - 1
                else:
                    row = np.flatnonzero(self.field[:, column] >= 0)[0] - 1
                self.field[row, column] = player
                return 0

    def check_win(self, player: int) -> bool:
        players_dots = (self.field == player).astype(int)
        horizontal_map = convolve1d(players_dots, [1, 1, 1, 1], axis=1, mode='constant')
        vertical_map = convolve1d(players_dots, [1, 1, 1, 1], axis=0, mode='constant')
        diagonal_map_f = convolve(players_dots, np.eye(4), mode='constant')
        diagonal_map_s = convolve(players_dots, np.flip(np.eye(4), axis=1), mode='constant')
        return max(horizontal_map.max(), vertical_map.max(), diagonal_map_f.max(), diagonal_map_s.max()) >= 4
    
    def check_desk_full(self) -> bool:
        return np.sum(self.field == -1) == 0

    def find_winner(self) -> int:
        for i in range(self.num_players):
            if self.check_win(i):
                return i
        return -1
    
    def print_field(self):
        
        for row in self.field:
            print(" ".join(np.char.mod("%.2f", row)))
