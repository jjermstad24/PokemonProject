from src.move import Move
from src.ptype import Type


def test_move_has_attributes():
    move = Move("Tackle", Type.NORMAL, 40, 100, 35)
    assert move.name == "Tackle"
    assert move.ptype == Type.NORMAL
    assert move.power == 40


def test_use_is_callable():
    move = Move("Tackle", Type.NORMAL, 40, 100, 35)
    assert isinstance(move.use(), bool)
