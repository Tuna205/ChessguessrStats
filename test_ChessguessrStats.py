from ChessguessrStats import ChessguessrStats
import pytest

class TestChessguessrStats:
    def setup_method(self, method):
        self.stats = ChessguessrStats()

    def test_parse_gamedle_try(self):
        assert self.stats.parse_gamedle_try('🟥🟥🟥🟥🟥🟥') == -1
        assert self.stats.parse_gamedle_try('🟩⬜⬜⬜⬜⬜') == 1
        assert self.stats.parse_gamedle_try('🟥🟥🟩⬜⬜⬜') == 3


    def test_parse_squares_from_line(self):
        assert self.stats.parse_squares_from_line('🕹️🎨 Gamedle (Artwork mode): 08/12/2023 🟥🟥🟥🟥🟥🟥 ') == '🟥🟥🟥🟥🟥🟥'
        assert self.stats.parse_squares_from_line('🕹️🔑 Gamedle (keywords mode): 11/12/2023 🟥🟥🟥🟥🟥🟩 - trebao sam puno ranije pogoditi') == '🟥🟥🟥🟥🟥🟩'
        assert self.stats.parse_squares_from_line('test') == ''

    def test_parse_gamedle_line(self):
        assert self.stats.parse_gamedle_line('12/12/23, 07:49 - Antun: 🕹️ Gamedle: 12/12/2023 🟥🟥🟥🟥🟥🟩') == {'Classic' : 6}
        assert self.stats.parse_gamedle_line('🕹️🎨 Gamedle (Artwork mode): 12/12/2023 🟥🟥🟥🟥🟥🟥 ') == {'Art' : -1}
        assert self.stats.parse_gamedle_line('🕹️🔑 Gamedle (keywords mode): 12/12/2023 🟥🟥🟥🟥🟩⬜') == {'Keywords' : 5}
        assert self.stats.parse_gamedle_line('test') == {}