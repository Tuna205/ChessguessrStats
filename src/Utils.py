from datetime import datetime
import pandas as pd


class Utils:

    @staticmethod
    def to_date(date_str):
        date = datetime.strptime(date_str, '%m/%d/%y')
        return date

    @staticmethod
    def create_dataframe(master_dict):
        df_dict = {}
        for player, stats in master_dict.items():
            df_dict[player] = pd.DataFrame(stats).T
        return df_dict

    @staticmethod
    def create_num_tries_dataframe(num_tries_dict):
        df_dict = {}
        for player, stats in num_tries_dict.items():
            df = pd.DataFrame(stats)
            df_dict[player] = df
        return df_dict

    @staticmethod
    def create_total_tries_dataframe(total_tries_dict):
        df = pd.DataFrame(total_tries_dict)
        return df
