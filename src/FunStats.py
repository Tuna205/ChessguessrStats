from src.Constants import GameMode, FAILED_TRY


class FunStats:

    def __init__(self, master_dict):
        self.master_dict = master_dict

    def create_num_tries_dict(self):
        return {GameMode.Classic: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, FAILED_TRY: 0},
                GameMode.Art: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, FAILED_TRY: 0},
                GameMode.Keywords: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, FAILED_TRY: 0},
                GameMode.Chessguessr: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, FAILED_TRY: 0}, }

    def number_of_tries(self):
        number_of_tries = {}
        for player, sub_dict in self.master_dict.items():
            number_of_tries[player] = self.create_num_tries_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    number_of_tries[player][game_mode][score] += 1

        return number_of_tries

    def create_total_try_dict(self):
        return {GameMode.Classic: 0,
                GameMode.Art: 0,
                GameMode.Keywords: 0,
                GameMode.Chessguessr: 0}

    def total_tries(self):
        total_tries = {}
        for player, sub_dict in self.master_dict.items():
            total_tries[player] = self.create_total_try_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    total_tries[player][game_mode] += score
        return total_tries

    def create_top_3_dict(self):
        return {GameMode.Classic: [],
                GameMode.Art: [],
                GameMode.Keywords: [],
                GameMode.Chessguessr: []}

    def top_streak(self):  # chessguessr first try, gamedle before fail
        streaks = {}
        for player, sub_dict in self.master_dict.items():
            streaks[player] = self.create_top_3_dict()
            current_streak = self.create_total_try_dict()
            for date, scores in sub_dict.items():
                for game_mode, score in scores.items():
                    if game_mode == GameMode.Chessguessr:
                        if score == 1:
                            current_streak[game_mode] += 1
                        elif current_streak[game_mode] != 0:
                            streaks[player][game_mode].append(
                                current_streak[game_mode])
                            current_streak[game_mode] = 0
                    else:
                        if score != FAILED_TRY:
                            current_streak[game_mode] += 1
                        elif current_streak[game_mode] != 0:
                            streaks[player][game_mode].append(
                                current_streak[game_mode])
                            current_streak[game_mode] = 0

            for game_mode, last_streak in current_streak.items():
                if last_streak != 0:
                    streaks[player][game_mode].append(last_streak)

        for player, sub_dict in streaks.items():
            for game_mode, streak in sub_dict.items():
                streak.sort(reverse=True)
                # streak[:3] za top3
                streaks[player][game_mode] = streak[0]

        return streaks

    def days_played(self):
        for player, sub_dict in self.master_dict.items():
            return len(sub_dict)
