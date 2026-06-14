from src.ptype import Type


class Move:
    def __init__(self, name: str, ptype: Type, power: int, accuracy: int, max_pp: int):
        self.name = name
        self.ptype = ptype
        self.power = power
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.current_pp = max_pp

    def use(self) -> bool:
        return True

    def reset_pp(self):
        ...

    def __repr__(self) -> str:
        return self.name
