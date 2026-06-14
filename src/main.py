from src.pokemon import Pokemon
from src.trainer import Trainer
from src.battle import Battle
from src.gui import BattleGUI


def main():
    charmander = Pokemon.from_species("Charmander", level=5)
    squirtle = Pokemon.from_species("Squirtle", level=5)

    player = Trainer("Player", [charmander])
    rival = Trainer("Rival", [squirtle])

    battle = Battle(player, rival)
    gui = BattleGUI(battle)
    gui.run()


if __name__ == "__main__":
    main()
