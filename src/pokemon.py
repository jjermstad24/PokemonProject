from src.ptype import Type
from src.move import Move


class Pokemon:
    def __init__(self, species: str, primary_type: Type, hp: int, attack: int, defense: int):
        self.species = species
        self.primary_type = primary_type
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = list[Move]()
        self.fainted = False
        self.level = 5

    @classmethod
    def from_species(cls, species: str, level: int = 5):
        from src.pokemon_data import POKEMON_DATA, MOVE_DATA
        pokemon = cls(species, POKEMON_DATA[species]['primary_type'], POKEMON_DATA[species]['base_hp'], POKEMON_DATA[species]['base_attack'], POKEMON_DATA[species]['base_defense'])
        pokemon.level = level
        pokemon.moves = [MOVE_DATA[move] for move in POKEMON_DATA[species]['moves']]
    
        return pokemon

    @property
    def types(self) -> list[Type]:
        return [self.primary_type]

    def take_damage(self, amount: int):
        ...

    def heal(self, amount: int):
        ...

    def is_fainted(self) -> bool:
        return self.fainted

    def __repr__(self) -> str:
        return f"{self.species} ({self.current_hp}/{self.max_hp} HP)"
