from typing import Optional

from src.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, party: Optional[list[Pokemon]] = None):
        self.name = name
        self.party = party or []

    def add_pokemon(self, pokemon: Pokemon):
        ...

    def first_available(self) -> Optional[Pokemon]:
        ...

    def has_available(self) -> bool:
        ...

    def __repr__(self) -> str:
        return f"Trainer {self.name}"
