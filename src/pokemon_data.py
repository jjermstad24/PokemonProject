from src.move import Move
from src.ptype import Type

MOVE_DATA = {
    "Scratch": Move(
        name="Scratch", 
        ptype=Type.NORMAL, 
        power=40, 
        accuracy=100, 
        max_pp=35),
    "Ember": Move(
        name="Ember", 
        ptype=Type.FIRE, 
        power=40, 
        accuracy=100, 
        max_pp=25),
    "Water Gun": Move(
        name="Water Gun", 
        ptype=Type.WATER, 
        power=40, 
        accuracy=100, 
        max_pp=25),
}

POKEMON_DATA = {
    "Charmander": {
        "primary_type": Type.FIRE,
        "base_hp": 39,
        "base_attack": 52,
        "base_defense": 43,
        "moves": ["Scratch", "Ember"],
    },
    "Squirtle": {
        "primary_type": Type.WATER,
        "base_hp": 44,
        "base_attack": 48,
        "base_defense": 65,
        "moves": ["Scratch", "Water Gun"],
    },
}
