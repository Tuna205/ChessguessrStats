from src.FunStats import FunStats
from src.DailyGameStats import GameMode, FAILED_TRY
from datetime import datetime


class TestFunStats:  # todo koristi game mode + fail tryes
    def setup_method(self, method):
        self.mock_master = {
            'Dino Ehman': {datetime(2023, 12, 4, 0, 0): {GameMode.Classic: 6, GameMode.Art: 5, GameMode.Keywords: FAILED_TRY, GameMode.Chessguessr: 1},
                           datetime(2023, 12, 5, 0, 0): {GameMode.Classic: 3, GameMode.Art: 4, GameMode.Keywords: FAILED_TRY, GameMode.Chessguessr: 2},
                           datetime(2023, 12, 6, 0, 0): {GameMode.Classic: FAILED_TRY, GameMode.Art: FAILED_TRY, GameMode.Keywords: 2, GameMode.Chessguessr: 4}},
            'Antun': {datetime(2023, 12, 4, 0, 0): {GameMode.Classic: 3, GameMode.Art: 6, GameMode.Keywords: 2, GameMode.Chessguessr: 1},
                      datetime(2023, 12, 5, 0, 0): {GameMode.Classic: FAILED_TRY, GameMode.Art: 5, GameMode.Keywords: 2, GameMode.Chessguessr: 3},
                      datetime(2023, 12, 6, 0, 0): {GameMode.Classic: 1, GameMode.Art: FAILED_TRY, GameMode.Keywords: 2, GameMode.Chessguessr: 2}}
        }
        self.fun_stats = FunStats(self.mock_master)

    def test_number_of_tries(self):
        assert self.fun_stats.number_of_tries()['Dino Ehman'] == {GameMode.Classic: {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 1, FAILED_TRY: 1},
                                                                  GameMode.Art: {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 0, FAILED_TRY: 1},
                                                                  GameMode.Keywords: {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, FAILED_TRY: 2},
                                                                  GameMode.Chessguessr: {1: 1, 2: 1, 3: 0, 4: 1, 5: 0, FAILED_TRY: 0}}

    def test_total_tries(self):
        assert self.fun_stats.total_tries()['Dino Ehman'] == {GameMode.Classic: 19,
                                                              GameMode.Art: 19,
                                                              GameMode.Keywords: 22,
                                                              GameMode.Chessguessr: 7}

    def test_top_3_streaks(self):
        assert self.fun_stats.top_3_streaks()['Antun'] == {GameMode.Classic: [1, 1],
                                                           GameMode.Art: [2],
                                                           GameMode.Keywords: [3],
                                                           GameMode.Chessguessr: [1]}

    def test_days_played(self):
        assert self.fun_stats.days_played() == 3
