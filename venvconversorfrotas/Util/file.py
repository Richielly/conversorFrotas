import pandas as pd
class File:

    def file_read(self, file):
        df = pd.read_csv(file, sep='|', header=None, encoding='ansi')
        df.index = range(1, len(df) + 1)
        df = df.drop(df.shape[1]-1, axis=1)
        df = df.fillna(value='')

        return df

    def file_size(self, df_file):
        return df_file.shape[0]

    def file_colum_size(self, df_file):
        return df_file.shape[1]

    def lines_file(self, df_file, line=None):
        if not line:
            return df_file.values
        else:
            return df_file.values[line - 1]
