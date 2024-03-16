
# fun stats - can be calculated from a date
#     - top 3 biggest streaks for every mode
#     - number of tries graph
#     - total number of tries
#     - perfection
#     - total fail
#     - biggest differences - ako se može dobiti referenca na konkretanu pazlu
from DailyGameStats import GameMode

class FunStats:
    
    def __init__(self, master_dict):
        self.master_dict = master_dict
        self.FAILED_TRY = 10

    def create_game_dict(self):
        return {GameMode.Classic : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Art : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Keywords : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Chessguessr : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, self.FAILED_TRY: 0},}

    def number_of_tries(self):
        number_of_tries = {}
        for player, sub_dict in self.master_dict.items():
            number_of_tries[player] = self.create_game_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    number_of_tries[player][game_mode][score] += 1

        return number_of_tries


    