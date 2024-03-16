
# fun stats - can be calculated from a date
#     - top 3 biggest streaks for every mode
#     - number of tries graph
#     - total number of tries
# slice -----------
#     - perfection
#     - total fail
#     - biggest differences - ako se može dobiti referenca na konkretanu pazlu
from DailyGameStats import GameMode

class FunStats:
    
    def __init__(self, master_dict):
        self.master_dict = master_dict
        self.FAILED_TRY = 10

    def create_num_tries_dict(self):
        return {GameMode.Classic : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Art : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Keywords : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, self.FAILED_TRY: 0},
                GameMode.Chessguessr : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, self.FAILED_TRY: 0},}

    def number_of_tries(self):
        number_of_tries = {}
        for player, sub_dict in self.master_dict.items():
            number_of_tries[player] = self.create_num_tries_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    number_of_tries[player][game_mode][score] += 1

        return number_of_tries
    
    def create_total_try_dict(self):
        return {'Classic' : 0,
                'Art' : 0,
                'Keywords' : 0,
                'Chessguessr' : 0}
    
    def total_tries(self):
        total_tries = {}
        for player, sub_dict in self.master_dict.items():
            total_tries[player] = self.create_total_try_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    total_tries[player][game_mode] += score
        return total_tries

    