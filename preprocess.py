import pandas as pd
import numpy as np

def standard(std_df):
    std = std_df[std_df['taiff'] == "E"]
    std = std.reset_index()
    std = std[['ID']]
    return std


if __name__ == "__main__":
    std_df = pd.read_csv("/daintlab/data/CER_electricity/SR_allocations.csv")
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
    id_list = standard(std_df)
    ex_list = pd.merge(id_list, file_df, on='ID', how='inner')

    pv_list = pd.pivot_table(ex_list,
                             index='ID',
                             columns='DT',
                             values='Usage'
                            )
    
    pv_list.insert(12339, 45202, None)
    pv_list.insert(12340, 45203, None)

    pv_list = pv_list.drop([29849, 29850, 66949, 66950], axis=1)
    pv_list = pv_list.T

    

    print(pv_list.shape)
    pv_list.to_csv("/daintlab/data/CER_electricity/new_data.csv")
    #print(pv_list.shape)
    #print(pv_list.head())
    #print(pv_list.isnull().sum().sum())
    #pv_list = pv_list.T
    #print(pv_list.shape)
    #pv_list = pv_list.interpolate('linear')    
    #print(pv_list.isnull().sum().sum())
    #pv_list = pv_list.T
    #print(pv_list.shape)
    
    '''
    id_list = standard(std_df)
    ex_list = pd.merge(id_list, file_df, on='ID', how='inner')

    ex_list['NEW_DT'] = pd.to_datetime(ex_list['DT'])
    print(ex_list.head())

    print(ex_list.shape)

    pv_list = pd.pivot_table(ex_list,
                             index='ID',
                             columns='DT',
                             values='Usage'
                            )
    
    #print(pv_list.shape)
    print(pv_list.head())

    #print(pv_list.isnull().sum().sum())
    pv_list = pv_list.T
    #print(pv_list.shape)
    pv_list = pv_list.interpolate('linear')    
    #print(pv_list.isnull().sum().sum())
    pv_list = pv_list.T
    #print(pv_list.shape)
    #pv_list.to_csv("/daintlab/data/CER_electricity/tsdata.csv")
'''
