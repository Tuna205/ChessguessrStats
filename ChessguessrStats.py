import codecs
import re


class ChessguessrStats:
    def __init__(self):
        self.current_name = ''
        self.current_date = ''
        self.master_dict = {}

    def parse_gamedle_try(self, squares):
        for i, square in enumerate(squares):
            if square == '🟩':
                return i + 1
        return -1

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

    def main(self):
        lines = self.read_file()
        for line in lines:
            parsed_header = self.parse_message_header(line)
            if (parsed_header):
                self.current_date, time, self.current_name = parsed_header
                if self.current_name not in self.master_dict:
                    self.master_dict[self.current_name] = {}
                if self.current_date not in self.master_dict[self.current_name]:
                    self.master_dict[self.current_name][self.current_date] = {}
                self.create_gamedle_entry(line)
            else:
                self.create_gamedle_entry(line)

stats = ChessguessrStats()
stats.main()
print(stats.master_dict)


# kako exportati - csv: datum | gamedle classic | gamedle art | gamedle keywords | chessguess