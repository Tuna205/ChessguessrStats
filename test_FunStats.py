from FunStats import FunStats
from DailyGameStats import GameMode
import pytest
from datetime import datetime

class TestFunStats: # todo koristi game mode + fail tryes
    def setup_method(self, method):
        self.mock_master = {
            'Dino Ehman': { datetime(2023, 12, 4, 0, 0): {'Classic': 6, 'Art': 5, 'Keywords': 10, 'Chessguessr': 1},
                            datetime(2023, 12, 5, 0, 0): {'Classic': 3, 'Art': 4, 'Keywords': 10, 'Chessguessr': 2},
                            datetime(2023, 12, 6, 0, 0): {'Classic': 10, 'Art': 10, 'Keywords': 2, 'Chessguessr': 4}},
            'Antun': { datetime(2023, 12, 4, 0, 0): {'Classic': 3, 'Art': 6, 'Chessguessr': 1},
                       datetime(2023, 12, 5, 0, 0): {'Classic': 10, 'Art': 5, 'Keywords': 2, 'Chessguessr': 3},
                       datetime(2023, 12, 6, 0, 0): {'Classic': 1, 'Art': 10, 'Keywords': 2, 'Chessguessr': 2}}
        }
        self.fun_stats = FunStats(self.mock_master)

    def test_number_of_tries(self):
        assert self.fun_stats.number_of_tries()['Dino Ehman'] == {  'Classic' : {1 : 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 1, 10: 1},
                                                                    'Art' : {1 : 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 0, 10: 1},
                                                                    'Keywords' : {1 : 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 10: 2},
                                                                    'Chessguessr' : {1 : 1, 2: 1, 3: 0, 4: 1, 5: 0, 10: 0}}
        
        