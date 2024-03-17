from src.FunStats import FunStats
from src.GraphCreator import GraphCreator
from src.Constants import GameMode
from src.Utils import Utils
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QScrollArea
import sys
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
        df_dict = Utils.create_dataframe(master_dict)
        classic_plot = GraphCreator.create_game_mode_graph(
            GameMode.Classic, df_dict)
        art_plot = GraphCreator.create_game_mode_graph(GameMode.Art, df_dict)
        keyword_plot = GraphCreator.create_game_mode_graph(
            GameMode.Keywords, df_dict)
        chessguessr_plot = GraphCreator.create_game_mode_graph(
            GameMode.Chessguessr, df_dict)

        classic_canvas = MplCanvas(*classic_plot, self)
        classic_toolbar = NavigationToolbar(classic_canvas, self)

        art_canvas = MplCanvas(*art_plot, self)
        art_toolbar = NavigationToolbar(art_canvas, self)

        keyword_canvas = MplCanvas(*keyword_plot, self)
        keyword_toolbar = NavigationToolbar(keyword_canvas, self)

        chessguessr_canvas = MplCanvas(*chessguessr_plot, self)
        chessguessr_toolbar = NavigationToolbar(chessguessr_canvas, self)

        num_of_tries_wgt = self.create_num_of_tries_widget()

        layout = QtWidgets.QVBoxLayout()

        num_of_tries_title = QLabel("Number of tries", self)
        layout.addWidget(num_of_tries_title)
        layout.addWidget(num_of_tries_wgt)

        daily_title = QLabel("Daily Tries", self)
        layout.addWidget(daily_title)
        # layout.addWidget(classic_toolbar)
        layout.addWidget(classic_canvas)

        # layout.addWidget(art_toolbar)
        layout.addWidget(art_canvas)

        # layout.addWidget(keyword_toolbar)
        layout.addWidget(keyword_canvas)

        # layout.addWidget(chessguessr_toolbar)
        layout.addWidget(chessguessr_canvas)

        root = QtWidgets.QWidget()
        root.setLayout(layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(root)

        self.setWindowTitle("Game Stats")
        self.setCentralWidget(scroll_area)

        self.showMaximized()

    def create_num_of_tries_widget(self):
        fun_stats = FunStats(self.master_dict)
        num_tries = fun_stats.number_of_tries()
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
