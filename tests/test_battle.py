from src.pokemon import Pokemon
from src.trainer import Trainer
from src.battle import Battle
from src.ptype import Type


def test_battle_constructs():
    charmander = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    squirtle = Pokemon("Squirtle", Type.WATER, 44, 48, 65)
    player = Trainer("P", [charmander])
    opponent = Trainer("O", [squirtle])
    battle = Battle(player, opponent)
    assert isinstance(battle, Battle)


def test_is_over_starts_false():
    charmander = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    squirtle = Pokemon("Squirtle", Type.WATER, 44, 48, 65)
    player = Trainer("P", [charmander])
    opponent = Trainer("O", [squirtle])
    battle = Battle(player, opponent)
    assert battle.is_over() is False
