import codecs
import re
import pandas as pd
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt

class ChessguessrStats:
    def __init__(self):
        self.current_name = ''
        self.current_date = ''
        self.master_dict = {}
        self.FAILED_TRY = 10

    def parse_gamedle_try(self, squares):
        for i, square in enumerate(squares):
            if square == '🟩':
                return i + 1
        return self.FAILED_TRY

    def parse_squares_from_line(self, line):
        pattern = r"[🟩🟨⬜🟥]+"
        matches = re.findall(pattern, line)
        if matches:
            return matches[0]
        else:
            return None

    def parse_gamedle_line(self, line):
        if ('🕹️ Gamedle:' in line):
            return 'Classic'
        elif ('🕹️🎨 Gamedle (Artwork mode):' in line):
            return 'Art'
        elif ('🕹️🔑 Gamedle (keywords mode):' in line):
            return 'Keywords'
        else:
            return None

    def parse_message_header(self, line):
        pattern = r"\d+/\d+/\d+, \d+:\d+ - [\w ]+:"
        matches = re.findall(pattern, line)
        if matches:
            split_comma = matches[0].split(',')
            date = split_comma[0]
            split_dash = split_comma[1].split('-')
            time = split_dash[0].strip()
            name = split_dash[1].strip()[:-1]
            return (date, time, name)
        else:
            return None

    def read_file(self):
        with codecs.open('data/WhatsApp Chat with Dino Ehman.txt', encoding='utf-8') as file:
            lines = file.readlines()
            return lines

    def create_gamedle_entry(self, line):
        gamedle_type = self.parse_gamedle_line(line)
        if gamedle_type:
            squares = self.parse_squares_from_line(line)
            try_num = self.parse_gamedle_try(squares)             
            self.master_dict[self.current_name][self.current_date][gamedle_type] =  try_num
            return True
        else:
            return False

    def setup_master_entry(self, parsed_header):
        self.current_date, time, self.current_name = parsed_header
        if self.current_name not in self.master_dict:
            self.master_dict[self.current_name] = {}
        if self.current_date not in self.master_dict[self.current_name]:
            self.master_dict[self.current_name][self.current_date] = {}

    def create_dataframe(self):
        df_dict = {}
        for player, stats in self.master_dict.items():
            df_dict[player] = pd.DataFrame(stats).T
        return df_dict

    def export_to_excel(self, file_name):
        master_df = self.create_dataframe()
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        for sheet_name, df in master_df.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.close()

    def clean_master_dict(self):
        for_deletion = []
        for player, sub_dict in self.master_dict.items():
            for date, scores in sub_dict.items():
                if scores == {}:
                    for_deletion.append((player, date))
        
        for player, date in for_deletion:
            del self.master_dict[player][date]

    def create_graph(self):
        df_dict = self.create_dataframe()
        fig, ax = plt.subplots()
        dates = self.calculate_all_playing_dates()
        dates_index = pd.Index(dates)
        for player, df in df_dict.items():
            ax.bar(df.index, df["Classic"]) # TODO use dates_index, wrong shape for dataframe
            # plt.title(player)
        ax.set_xlabel("Date")
        ax.set_ylabel("Tries")
        ax.legend()
        plt.show()

    def calculate_all_playing_dates(self):
        dates = []
        for player, sub_dict in self.master_dict.items():
            for date in sub_dict:
                dates.append(date)
        return list(dict.fromkeys(dates))

    def unify_dates(self):
        dates = self.calculate_all_playing_dates()
        for player, sub_dict in self.master_dict.items():
            for date in dates:
                if date not in sub_dict:
                    sub_dict[date] = {'Classic' : 0, 'Art' : 0, 'Keywords' : 0, 'Chessguesser' : 0} 

    def main(self):
        lines = self.read_file()
        for line in lines:
            parsed_header = self.parse_message_header(line)
            if (parsed_header):
                self.setup_master_entry(parsed_header)
                self.create_gamedle_entry(line)
            else:
                self.create_gamedle_entry(line)
        self.clean_master_dict()
        self.unify_dates()

stats = ChessguessrStats()
stats.main()
# print(stats.master_dict['Dino Ehman'])
# print('########')
# print(stats.master_dict['Antun'])
dfs = stats.create_dataframe()
antun_df = dfs['Antun']
dino_df = dfs['Dino Ehman']
# stats.export_to_excel("test_export.xlsx")
# print(plt.matplotlib_fname())
stats.create_graph()

### todo expot date to excell, vjerojatno treba samo exportati index