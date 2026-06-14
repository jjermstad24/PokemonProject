from src.ptype import Type, get_effectiveness


def test_type_enum_has_values():
    assert Type.NORMAL == "Normal"
    assert Type.FIRE == "Fire"
    assert Type.WATER == "Water"


def test_get_effectiveness_is_callable():
    result = get_effectiveness(Type.FIRE, Type.GRASS)
    assert isinstance(result, float)
