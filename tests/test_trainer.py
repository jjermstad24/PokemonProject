from src.trainer import Trainer
from src.pokemon import Pokemon
from src.ptype import Type


def test_trainer_has_name():
    trainer = Trainer("Ash")
    assert trainer.name == "Ash"


def test_trainer_starts_with_empty_party():
    trainer = Trainer("Ash")
    assert trainer.party == []


def test_trainer_can_take_party():
    p = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    trainer = Trainer("Ash", [p])
    assert p in trainer.party
