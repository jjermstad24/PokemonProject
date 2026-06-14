from src.battle import Battle
from src.pokemon import Pokemon
from src.move import Move


def show_battle_status(battle: Battle):
    p = battle.player_active
    o = battle.opponent_active
    print(f"\n{'='*40}")
    print(f"{battle.opponent.name}")
    print(f"  {o.species}  HP: {o.current_hp}/{o.max_hp}")
    print(f"{'─'*40}")
    print(f"{battle.player.name}")
    print(f"  {p.species}  HP: {p.current_hp}/{p.max_hp}")
    print(f"{'='*40}")


def show_moves(pokemon: Pokemon):
    print(f"\n{pokemon.species}'s moves:")
    for i, move in enumerate(pokemon.moves, 1):
        print(f"  {i}. {move}")


def get_player_choice(pokemon: Pokemon) -> tuple[str, object]:
    while True:
        show_moves(pokemon)
        try:
            choice = int(input("\nChoose a move (1-4): "))
            if 1 <= choice <= len(pokemon.moves):
                return "move", pokemon.moves[choice - 1]
        except ValueError:
            pass
        print("Invalid choice.")


def show_log(battle: Battle):
    for line in battle.log:
        print(f"  {line}")
    battle.log.clear()
