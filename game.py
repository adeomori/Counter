import numpy as np
from field import Field

class Game:
    def __init__(self, height: int, width: int, num_players: int) -> None:
        self.height = height
        self.width = width
        self.num_players = num_players
        self.field = Field(height, width, num_players)
        print(f"CREATED GAME WITH {self.num_players} players on field {self.height}x{self.width}")
        self.field.print_field()
        self.player = 0
    
    def make_turn(self) -> int:
        print(f"NOW IT IS {self.player + 1}-TH PLAYERS TURN, CHOOSE COLUMN (1-{self.width}):")
        print("_".join( (np.arange(self.width) + 1).astype(str)))
        while True:
            players_input = int(input()) - 1
            turn_result = self.field.turn(players_input, self.player)
            if turn_result == 0:
                print("DESK AFTER TURN:")
                self.field.print_field()
                break
            elif turn_result == 1:
                print("COLUMN OUT OF BOUNDS, PLEASE TRY AGAIN")
            elif  turn_result == 2:
                print("COLUMN IS FULL, PLEASE TRY ANOTHER ONE")
        if self.field.check_win(self.player):
            print(f"{self.player+1} PLAYER WINS!!!")    
            return 0
        elif self.field.check_desk_full():
            print("DESK IS FULL, GAME OVER")
            return 0
        self.player = (self.player + 1) % self.num_players
        return 1    
    
    def run_game_loop(self) -> None:
        while True:
            if self.make_turn() == 0:
                break

