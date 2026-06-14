from src.ptype import Type


class Pokemon:
    def __init__(self, species: str, primary_type: Type, hp: int, attack: int, defense: int):
        self.species = species
        self.primary_type = primary_type
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = []
        self.fainted = False
        self.level = 5

    @classmethod
    def from_species(cls, species: str, level: int = 5):
        pokemon = cls(species, Type.NORMAL, 1, 1, 1)
        pokemon.level = level
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
