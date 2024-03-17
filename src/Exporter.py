import pandas as pd

class Exporter:

    @staticmethod
    def export_to_excel(dict_of_dfs, file_name):
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        for sheet_name, df in dict_of_dfs.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.close()