import codecs
import re


class ChessguessrStats:
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
            return ''

    def parse_gamedle_line(self, line):
        squares = self.parse_squares_from_line(line)
        try_num = self.parse_gamedle_try(squares)

        if ('🕹️ Gamedle:' in line):
            return {'Classic' : try_num}
        elif ('🕹️🎨 Gamedle (Artwork mode):' in line):
            return {'Art' : try_num}
        elif ('🕹️🔑 Gamedle (keywords mode):' in line):
            return {'Keywords' : try_num}
        else:
            return {}

    def main():


        with codecs.open('WhatsApp Chat with Dino Ehman.txt', encoding='utf-8') as file:

            lines = file.readlines()

            count = 0
            for line in lines:

                if ('Gamedle:' in line):

                    gamedle = ''




# kako exportati - csv: datum | gamedle classic | gamedle art | gamedle keywords | chessguessr