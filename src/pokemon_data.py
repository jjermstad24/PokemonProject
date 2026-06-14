from src.ptype import Type

MOVE_DATA = {
    "Scratch": {"ptype": Type.NORMAL, "power": 40, "accuracy": 100, "max_pp": 35},
    "Ember": {"ptype": Type.FIRE, "power": 40, "accuracy": 100, "max_pp": 25},
    "Water Gun": {"ptype": Type.WATER, "power": 40, "accuracy": 100, "max_pp": 25},
}

POKEMON_DATA = {
    "Charmander": {
        "primary_type": Type.FIRE,
        "base_hp": 39,
        "base_attack": 52,
        "base_defense": 43,
    },
}
