import pandas as pd

def standard(std_df):
    std = std_df[std_df['taiff'] == "E"]
    std = std.reset_index()
    std = std[['ID']]
    return std


if __name__ == "__main__":
    std_df = pd.read_csv("C:/Users/USER/programming/data/SR_allocations.csv")
    file1 = pd.read_csv("C:/Users/USER/programming/data/File1.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file2 = pd.read_csv("C:/Users/USER/programming/data/File2.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file3 = pd.read_csv("C:/Users/USER/programming/data/File3.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file4 = pd.read_csv("C:/Users/USER/programming/data/File4.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file5 = pd.read_csv("C:/Users/USER/programming/data/File5.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file6 = pd.read_csv("C:/Users/USER/programming/data/File6.txt",
                        sep=' ', names=['ID', 'DT', 'Usage'])
    file_df = pd.concat([file1, file2, file3, file4, file5, file6])
    id_list = standard(std_df)
    ex_list = pd.merge(id_list, file_df, on='ID', how='inner')

    pv_list = pd.pivot_table(ex_list,
                             index='ID',
                             columns='DT',
                             values='Usage'
                            )
    print(pv_list.head())
    pv_list.to_csv("tsdata.csv")
