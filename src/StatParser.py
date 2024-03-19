import codecs
import re
from src.Utils import Utils
from src.Constants import GameMode, FAILED_TRY


class StatParser:
    def __init__(self):
        self.current_name = ''
        self.current_date = ''
        self.master_dict = {}

    def parse_file(self, file_path):
        lines = self.read_file(file_path)
        for line in lines:
            parsed_header = self.parse_message_header(line)
            if (parsed_header):
                self.setup_master_entry(parsed_header)
            success = self.create_gamedle_entry(line)
            if not success:
                try_num = self.parse_chessguessr_line(line)
                if try_num != None:
                    self.create_chessguessr_entry(try_num)

        self.clean_master_dict()
        self.unify_dates()

    def parse_gamedle_try(self, squares):
        for i, square in enumerate(squares):
            if square == '🟩':
                return i + 1
        return FAILED_TRY

    def parse_squares_from_line(self, line):
        pattern = r"[🟩🟨⬜🟥]+"
        matches = re.findall(pattern, line)
        if matches:
            return matches[0]
        else:
            return None

    def parse_gamedle_line(self, line):
        if ('🕹️ Gamedle:' in line):
            return GameMode.Classic
        elif ('🕹️🎨 Gamedle (Artwork mode):' in line):
            return GameMode.Art
        elif ('🕹️🔑 Gamedle (keywords mode):' in line):
            return GameMode.Keywords
        else:
            return None

    def parse_message_header(self, line):
        pattern = r"\d+/\d+/\d+, \d+:\d+ - [\w ]+:"
        matches = re.findall(pattern, line)
        if matches:
            split_comma = matches[0].split(',')
            date = Utils.to_date(split_comma[0])
            split_dash = split_comma[1].split('-')
            time = split_dash[0].strip()
            name = split_dash[1].strip()[:-1]
            return (date, time, name)
        else:
            return None

    def create_gamedle_entry(self, line):
        gamedle_type = self.parse_gamedle_line(line)
        if gamedle_type:
            squares = self.parse_squares_from_line(line)
            try_num = self.parse_gamedle_try(squares)
            self.master_dict[self.current_name][self.current_date][gamedle_type] = try_num
            return True
        else:
            return False

    def setup_master_entry(self, parsed_header):
        self.current_date, time, self.current_name = parsed_header
        if self.current_name not in self.master_dict:
            self.master_dict[self.current_name] = {}
        if self.current_date not in self.master_dict[self.current_name]:
            self.master_dict[self.current_name][self.current_date] = {}

    def clean_master_dict(self):
        for_deletion = []
        for player, sub_dict in self.master_dict.items():
            for date, scores in sub_dict.items():
                if scores == {} or len(scores) != 4:
                    for_deletion.append((player, date))

        for player, date in for_deletion:
            del self.master_dict[player][date]

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
                    sub_dict[date] = {GameMode.Classic: FAILED_TRY,
                                      GameMode.Art: FAILED_TRY,
                                      GameMode.Keywords: FAILED_TRY,
                                      GameMode.Chessguessr: FAILED_TRY}

    def parse_chessguessr_line(self, line):
        pattern = r"\w*Chessguessr #\d+ ./\d"
        matches = re.findall(pattern, line)
        if matches:
            match = matches[0]
            split_space = match.split(' ')
            try_num = split_space[-1].split('/')[0]
            if try_num == 'X':
                try_num = FAILED_TRY
            return int(try_num)
        else:
            return None

    def create_chessguessr_entry(self, try_num):
        self.master_dict[self.current_name][self.current_date][GameMode.Chessguessr] = try_num

    def read_file(self, file_path):
        with codecs.open(file_path, encoding='utf-8') as file:
            lines = file.readlines()
            return lines
