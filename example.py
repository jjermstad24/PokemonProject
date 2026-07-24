
from src.pokemon import Pokemon
from src.trainer import Trainer
from src.battle import Battle
charmander = Pokemon.from_species('Charmander', 5)
squirtle = Pokemon.from_species('Squirtle', 5)
player = Trainer('Player', [charmander])
rival = Trainer('Rival', [squirtle])
battle = Battle(player, rival)
player_move = charmander.moves[0]
opponent_move = squirtle.moves[0]
battle.execute_turn(player_move, opponent_move)
for line in battle.log:
    print(line)
print(f'Charmander HP: {charmander.current_hp}/{charmander.max_hp}')
print(f'Squirtle HP: {squirtle.current_hp}/{squirtle.max_hp}')
print(f'Battle over: {battle.is_over()}')
