from datetime import timedelta
import matplotlib.pyplot as plt


class GraphCreator:

    @staticmethod
    def create_game_mode_graph(game_mode, df_dict):
        fig, ax = plt.subplots()
        width = 0.2
        day_width = timedelta(days=width)

        i = 0
        for player, df in df_dict.items():
            rect = ax.bar(df.index + day_width * i - day_width/2,
                          df[game_mode], label=player, width=width)
            ax.bar_label(rect, label_type='edge')
            i += 1

        plt.title(game_mode)
        ax.set_xlabel('Date')
        ax.set_ylabel('Tries')

        return (fig, ax)

    @staticmethod
    def create_num_tries_graph(game_mode, df_dict):
        fig, ax = plt.subplots()
        height = 0.4
        i = 0
        for player, df in df_dict.items():
            rect = ax.barh(df.index + height * i - height/2,
                           df[game_mode], label=player, height=height)
            ax.bar_label(rect, label_type='edge')
            i += 1

        plt.title(game_mode)
        ax.set_xlabel('Score')
        ax.set_ylabel('Tries')

        return (fig, ax)

    @staticmethod
    def create_total_tries_graph(df):
        ax = df.plot.barh()
        for container in ax.containers:
            ax.bar_label(container)
        fig = ax.get_figure()

        ax.set_xlabel('Score')
        ax.set_ylabel('Mode')

        return (fig, ax)

    @staticmethod
    def create_streaks_graph(df):
        ax = df.plot.barh()
        for container in ax.containers:
            ax.bar_label(container)
        fig = ax.get_figure()

        ax.set_xlabel('Score')
        ax.set_ylabel('Mode')

        return (fig, ax)
