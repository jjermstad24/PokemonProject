from src.pokemon import Pokemon
from src.ptype import Type


def test_pokemon_has_attributes():
    p = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    assert p.species == "Charmander"
    assert p.primary_type == Type.FIRE
    assert p.max_hp == 39


def test_is_fainted_starts_false():
    p = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    assert p.is_fainted() is False


def test_types_property():
    p = Pokemon("Charmander", Type.FIRE, 39, 52, 43)
    assert p.types == [Type.FIRE]


def test_from_species_returns_pokemon():
    p = Pokemon.from_species("Charmander", 5)
    assert isinstance(p, Pokemon)
    assert p.level == 5
