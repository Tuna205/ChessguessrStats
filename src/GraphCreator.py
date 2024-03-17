from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QtAgg')


class GraphCreator:

    @staticmethod
    def create_game_mode_graph(game_mode, df_dict):
        fig, ax = plt.subplots()
        width = 0.2
        day_width = timedelta(days=width)

        i = 0
        for player, df in df_dict.items():
            ax.bar(df.index + day_width * i,
                   df[game_mode], label=player, width=width)
            i += 1

        plt.title(game_mode)
        ax.set_xlabel('Date')
        ax.set_ylabel('Tries')
        ax.legend()
        plt.show()
