from src.DailyGameStats import DailyGameStats, GameMode
import pytest
from datetime import datetime

class TestDailyGameStats:
    def setup_method(self, method):
        self.stats = DailyGameStats()

    def test_parse_gamedle_try(self):
        assert self.stats.parse_gamedle_try('🟥🟥🟥🟥🟥🟥') == self.stats.FAILED_TRY
        assert self.stats.parse_gamedle_try('🟩⬜⬜⬜⬜⬜') == 1
        assert self.stats.parse_gamedle_try('🟥🟥🟩⬜⬜⬜') == 3

    def test_parse_squares_from_line(self):
        assert self.stats.parse_squares_from_line('🕹️🎨 Gamedle (Artwork mode): 08/12/2023 🟥🟥🟥🟥🟥🟥 ') == '🟥🟥🟥🟥🟥🟥'
        assert self.stats.parse_squares_from_line('🕹️🔑 Gamedle (keywords mode): 11/12/2023 🟥🟥🟥🟥🟥🟩 - trebao sam puno ranije pogoditi') == '🟥🟥🟥🟥🟥🟩'
        assert self.stats.parse_squares_from_line('test') == None

    def test_parse_gamedle_line(self):
        assert self.stats.parse_gamedle_line('12/12/23, 07:49 - Antun: 🕹️ Gamedle: 12/12/2023 🟥🟥🟥🟥🟥🟩') == GameMode.Classic
        assert self.stats.parse_gamedle_line('🕹️🎨 Gamedle (Artwork mode): 12/12/2023 🟥🟥🟥🟥🟥🟥 ') == GameMode.Art
        assert self.stats.parse_gamedle_line('🕹️🔑 Gamedle (keywords mode): 12/12/2023 🟥🟥🟥🟥🟩⬜') == GameMode.Keywords
        assert self.stats.parse_gamedle_line('test') == None

    def test_parse_message_header(self):
        assert self.stats.parse_message_header('12/13/23, 07:49 - Antun: 🕹️ Gamedle: 13/12/2023 🟥🟥🟥🟥🟥🟩') == (self.stats.to_date('12/13/23'), '07:49', 'Antun') # mm/dd/yy
        assert self.stats.parse_message_header('12/13/23, 07:49 - Dino Ehman: 🕹️ Gamedle: 13/12/2023 🟥🟥🟥🟥🟥🟩') == (self.stats.to_date('12/13/23'), '07:49', 'Dino Ehman')
        assert self.stats.parse_message_header('test') == None

    def test_setup_master_entry(self):
        line = '12/13/23, 07:49 - Dino Ehman: 🕹️ Gamedle: 13/12/2023 🟥🟥🟥🟥🟥🟩'
        self.stats.setup_master_entry(self.stats.parse_message_header(line))
        assert self.stats.current_date == self.stats.to_date('12/13/23')
        assert self.stats.current_name == 'Dino Ehman'
        assert self.stats.master_dict == { 'Dino Ehman' : { self.stats.to_date('12/13/23') : {}}}

    def test_create_gamedle_entry(self):
        line = '12/13/23, 07:49 - Dino Ehman: 🕹️ Gamedle: 13/12/2023 🟥🟥🟥🟥🟥🟩'
        parsed_header = self.stats.parse_message_header(line)
        self.stats.setup_master_entry(self.stats.parse_message_header(line))
        assert self.stats.create_gamedle_entry(line) == True
        assert self.stats.master_dict == {'Dino Ehman' : {self.stats.to_date('12/13/23') : { GameMode.Classic : 6}} }
        assert self.stats.create_gamedle_entry('test') == False

    def test_clean_master_dict(self):
        master_dict_mock = {'Antun' : {'2/12/22': {}, '7/19/22': {}, '9/11/22': {}, '12/1/23': {GameMode.Classic: 1}, '12/2/23': {GameMode.Art : 2}}}
        self.stats.master_dict = master_dict_mock
        self.stats.clean_master_dict()
        assert self.stats.master_dict == {'Antun' : {'12/1/23': {GameMode.Classic: 1}, '12/2/23': {GameMode.Art : 2}}}

    def test_unify_dates(self):
        master_dict_mock = {'Antun' : { '9/11/22': {GameMode.Art : 1}, '12/1/23': {GameMode.Classic: 1}, '12/2/23': {GameMode.Art : 2}},
                            'Dino Ehman' : {'2/12/22': {GameMode.Art : 2}, '7/19/22': {GameMode.Art : 3}, '12/1/23': {GameMode.Classic: 1}, '12/2/23': {GameMode.Art : 2}}}
        self.stats.master_dict = master_dict_mock
        self.stats.unify_dates()
        assert len(self.stats.master_dict['Antun']) == len(self.stats.master_dict['Dino Ehman'])
        assert self.stats.master_dict['Antun'].keys() == self.stats.master_dict['Dino Ehman'].keys()

    def test_parse_chessguessr_line(self):
        assert self.stats.parse_chessguessr_line('12/27/23, 12:11 - Dino Ehman: Chessguessr #554 3/5') == 3
        assert self.stats.parse_chessguessr_line('12/27/23, 12:11 - Dino Ehman: Chessguessr #554 X/5') == self.stats.FAILED_TRY
        assert self.stats.parse_chessguessr_line('test') == None

        

# kako exportati - csv: datum | gamedle classic | gamedle art | gamedle keywords | chessguess   