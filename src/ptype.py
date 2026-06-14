from enum import StrEnum


class Type(StrEnum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECTRIC = "Electric"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"
    ICE = "Ice"


def get_effectiveness(move_type: Type, defender_type: Type) -> float:
    return 1.0


def get_multiplier_label(multiplier: float) -> str:
    return ""
