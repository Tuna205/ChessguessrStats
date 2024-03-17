import pandas as pd


class Exporter:

    @staticmethod
    def export_to_excel(df_dict, file_name):
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        for sheet_name, df in df_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.close()
