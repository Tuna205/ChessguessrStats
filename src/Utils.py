from datetime import datetime
import pandas as pd


class Utils:

    @staticmethod
    def to_date(date_str):
        date = datetime.strptime(date_str, '%m/%d/%y')
        return date

    @staticmethod
    def create_dataframe(d):
        df_dict = {}
        for player, stats in d.items():
            df_dict[player] = pd.DataFrame(stats).T
        return df_dict
