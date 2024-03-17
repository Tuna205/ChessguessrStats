from src.DailyGameStats import DailyGameStats, GameMode
from src.FunStats import FunStats
from src.Exporter import Exporter
from src.GraphCreator import GraphCreator
from src.Utils import Utils


parser = DailyGameStats()
file = 'data/WhatsApp Chat with Dino Ehman.txt'
parser.parse_file(file)
master_dict = parser.master_dict
df_dict = Utils.create_dataframe(master_dict)
# GraphCreator.create_game_mode_graph(GameMode.Classic, df_dict)
# GraphCreator.create_game_mode_graph(GameMode.Art, df_dict)
# GraphCreator.create_game_mode_graph(GameMode.Keywords, df_dict)
# GraphCreator.create_game_mode_graph(GameMode.Chessguessr, df_dict)

# Exporter.export_to_excel(df_dict, 'test.xlsx')

stats = FunStats(master_dict)
print('Number of tries')
for player, tries in stats.number_of_tries().items():
    print(f'{player} : {tries}')
print('Total tries')
for player, tries in stats.total_tries().items():
    print(f'{player} : {tries}')
print('Top 3')
for player, top_3 in stats.top_3_streaks().items():
    print(f'{player} : {top_3}')
