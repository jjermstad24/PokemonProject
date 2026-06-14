from src.battle import Battle
from src.ui import show_battle_status, get_player_choice, show_log


class Game:
    def __init__(self, battle: Battle):
        self.battle = battle

    def run(self):
        while not self.battle.is_over():
            show_battle_status(self.battle)
            _, player_move = get_player_choice(self.battle.player_active)
            opponent_move = self.battle.opponent_active.moves[0]
            self.battle.execute_turn(player_move, opponent_move)
            show_log(self.battle)
        winner = self.battle.winner.name
        print(f"\n{winner} wins the battle!")
