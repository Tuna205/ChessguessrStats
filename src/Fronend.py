from src.FunStats import FunStats
from src.GraphCreator import GraphCreator
from src.Constants import GameMode
from src.Utils import Utils
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QScrollArea
import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, fig, ax, parent=None):
        self.axes = ax
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, master_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.master_dict = master_dict
        self.fun_stats = FunStats(master_dict)

        layout = QtWidgets.QVBoxLayout()

        main_title = QLabel("Game Stats")
        main_title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(main_title)

        days_played_label = QLabel(
            f"Days played : {self.fun_stats.days_played()}")
        layout.addWidget(days_played_label)

        num_of_tries_title = QLabel("Number of tries", self)
        layout.addWidget(num_of_tries_title)
        num_of_tries_wgt = self.create_num_of_tries_widget()
        layout.addWidget(num_of_tries_wgt)

        total_tries_title = QLabel("Total tries", self)
        layout.addWidget(total_tries_title)
        total_tries_wgt = self.create_total_tries_widget()
        layout.addWidget(total_tries_wgt)

        streaks_title = QLabel("Highest Streak", self)
        layout.addWidget(streaks_title)
        streaks_wgt = self.create_highest_streak_widget()
        layout.addWidget(streaks_wgt)

        # daily_title = QLabel("Daily Tries", self)
        # layout.addWidget(daily_title)
        # daily_wgt = self.create_daily_stats_widget()
        # layout.addWidget(daily_wgt)

        root = QtWidgets.QWidget()
        root.setLayout(layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(root)

        self.setWindowTitle("Game Stats")
        self.setCentralWidget(scroll_area)

        self.showMaximized()

    def create_daily_stats_widget(self):
        df_dict = Utils.create_dataframe(self.master_dict)
        classic_plot = GraphCreator.create_game_mode_graph(
            GameMode.Classic, df_dict)
        art_plot = GraphCreator.create_game_mode_graph(GameMode.Art, df_dict)
        keyword_plot = GraphCreator.create_game_mode_graph(
            GameMode.Keywords, df_dict)
        chessguessr_plot = GraphCreator.create_game_mode_graph(
            GameMode.Chessguessr, df_dict)

        classic_canvas = MplCanvas(*classic_plot, self)
        art_canvas = MplCanvas(*art_plot, self)
        keyword_canvas = MplCanvas(*keyword_plot, self)
        chessguessr_canvas = MplCanvas(*chessguessr_plot, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(classic_canvas)
        layout.addWidget(art_canvas)
        layout.addWidget(keyword_canvas)
        layout.addWidget(chessguessr_canvas)

        daily_wgt = QtWidgets.QWidget()
        daily_wgt.setLayout(layout)

        return daily_wgt

    def create_num_of_tries_widget(self):
        num_tries = self.fun_stats.number_of_tries()
        df_dict_tries = Utils.create_num_tries_dataframe(num_tries)
        num_tries_plot_classic = GraphCreator.create_num_tries_graph(
            GameMode.Classic, df_dict_tries)
        num_tries_canvas_classic = MplCanvas(*num_tries_plot_classic, self)

        num_tries_plot_art = GraphCreator.create_num_tries_graph(
            GameMode.Art, df_dict_tries)
        num_tries_canvas_art = MplCanvas(*num_tries_plot_art, self)

        num_tries_plot_keywords = GraphCreator.create_num_tries_graph(
            GameMode.Keywords, df_dict_tries)
        num_tries_canvas_keywords = MplCanvas(*num_tries_plot_keywords, self)

        num_tries_plot_chessguessr = GraphCreator.create_num_tries_graph(
            GameMode.Chessguessr, df_dict_tries)
        num_tries_canvas_chessguessr = MplCanvas(
            *num_tries_plot_chessguessr, self)

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(num_tries_canvas_classic)
        layout.addWidget(num_tries_canvas_art)
        layout.addWidget(num_tries_canvas_keywords)
        layout.addWidget(num_tries_canvas_chessguessr)

        num_of_tries_wgt = QtWidgets.QWidget()
        num_of_tries_wgt.setLayout(layout)

        return num_of_tries_wgt

    def create_total_tries_widget(self):
        total_tries = self.fun_stats.total_tries()
        df_total_try = Utils.create_total_tries_dataframe(total_tries)
        total_tries_plot = GraphCreator.create_total_tries_graph(df_total_try)
        total_tries_wgt = MplCanvas(*total_tries_plot, self)

        return total_tries_wgt

    def create_highest_streak_widget(self):
        streaks = self.fun_stats.top_streak()
        df_streaks = Utils.create_streaks_dataframe(streaks)
        streaks_plot = GraphCreator.create_streaks_graph(df_streaks)
        streaks_wgt = MplCanvas(*streaks_plot, self)

        return streaks_wgt
