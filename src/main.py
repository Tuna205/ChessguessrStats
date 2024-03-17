from DailyGameStats import DailyGameStats, GameMode
from FunStats import FunStats

parser = DailyGameStats()
file = 'data/WhatsApp Chat with Dino Ehman.txt'
parser.parse_file(file)
# parser.create_graph(GameMode.Classic)
# parser.create_graph(GameMode.Art)
# parser.create_graph(GameMode.Keywords)
# parser.create_graph(GameMode.Chessguessr)

stats = FunStats(parser.master_dict)
print('Number of tries')
for player, tries in stats.number_of_tries().items():
    print(f'{player} : {tries}')
print('Total tries')
for player, tries in stats.total_tries().items():
    print(f'{player} : {tries}')
print('Top 3')
for player, top_3 in stats.top_3_streaks().items():
    print(f'{player} : {top_3}')
