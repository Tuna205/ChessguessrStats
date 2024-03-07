from ChessguessrStats import ChessguessrStats


def test_parse_gamedle_try():

    stats = ChessguessrStats()

    assert stats.parse_gamedle_try('🟥🟥🟥🟥🟥🟥') == -1
    assert stats.parse_gamedle_try('🟩⬜⬜⬜⬜⬜') == 1
    assert stats.parse_gamedle_try('🟥🟥🟩⬜⬜⬜') == 3


def test_parse_squares_from_line():
    stats = ChessguessrStats()
    assert stats.parse_squares_from_line('🕹️🎨 Gamedle (Artwork mode): 08/12/2023 🟥🟥🟥🟥🟥🟥 ') == '🟥🟥🟥🟥🟥🟥'
    assert stats.parse_squares_from_line('🕹️🔑 Gamedle (keywords mode): 11/12/2023 🟥🟥🟥🟥🟥🟩 - trebao sam puno ranije pogoditi') == '🟥🟥🟥🟥🟥🟩'
    assert stats.parse_squares_from_line('test') == ''

def test_parse_gamedle_line():
    stats = ChessguessrStats()
    assert stats.parse_gamedle_line('12/12/23, 07:49 - Antun: 🕹️ Gamedle: 12/12/2023 🟥🟥🟥🟥🟥🟩') == {'Classic' : 6}
    assert stats.parse_gamedle_line('🕹️🎨 Gamedle (Artwork mode): 12/12/2023 🟥🟥🟥🟥🟥🟥 ') == {'Art' : -1}
    assert stats.parse_gamedle_line('🕹️🔑 Gamedle (keywords mode): 12/12/2023 🟥🟥🟥🟥🟩⬜') == {'Keywords' : 5}
    assert stats.parse_gamedle_line('test') == {}