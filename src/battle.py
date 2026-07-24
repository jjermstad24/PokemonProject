from typing import Optional

from src.pokemon import Pokemon
from src.trainer import Trainer
from src.move import Move

class Battle:
    def __init__(self, player: Trainer, opponent: Trainer):
        self.player = player
        self.opponent = opponent
        self.player_active: Optional[Pokemon] = player.first_available()
        self.opponent_active: Optional[Pokemon] = opponent.first_available()
        self.winner: Optional[Trainer] = None
        self.log: list[str] = []

    def is_over(self) -> bool:
        return self.winner is not None

    def execute_turn(self, player_move: Move, opponent_move: Move):
        return None