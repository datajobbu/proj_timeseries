import pandas as pd
import numpy as np


def standard():
    std_df = pd.read_csv("/daintlab/data/CER_electricity/SR_allocations.csv")
    std = std_df[std_df['taiff'] == "E"]
    std = std.reset_index()
    std = std[['ID']]
    
    return std


def concat_file():
    file1 = pd.read_csv("/daintlab/data/CER_electricity/File1.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file2 = pd.read_csv("/daintlab/data/CER_electricity/File2.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file3 = pd.read_csv("/daintlab/data/CER_electricity/File3.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file4 = pd.read_csv("/daintlab/data/CER_electricity/File4.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file5 = pd.read_csv("/daintlab/data/CER_electricity/File5.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file6 = pd.read_csv("/daintlab/data/CER_electricity/File6.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file_df = pd.concat([file1, file2, file3, file4, file5, file6])
    
    return file_df


def interpolate(df):
    df.T
    df.interpolate('linear')
    df.T

    return df


def rename(ts_data):
    series_ts = pd.date_range('2009-07-14 00:00', '2010-12-31 23:30', periods=25728)
    list_ts = []

    for ts in series_ts:
        list_ts.append(ts)

    ts_data = ts_data.T
    ts_data['date_time'] = list_ts
    ts_data.set_index('date_time', inplace=True)

    ts_data = ts_data.T
    #ts_data = ts_data.drop('ID', axis=1)

    return ts_data


def main():
    id_list = standard()
    file_df = concat_file()
    ex_list = pd.merge(id_list, file_df, on='ID', how='inner')

    pv_list = pd.pivot_table(ex_list,
                             index='ID',
                             columns='DT',
                             values='Usage'
                            )    

    pv_list = pv_list.drop([73047, 73048], axis=1)
    
    pv_list = rename(pv_list)

    pv_list.to_csv("/daintlab/data/CER_electricity/new_data.csv")


if __name__ == "__main__":
    main()
