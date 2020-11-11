import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader


class TSData(Dataset):
    def __init__(self, data_frame, train=True):
        data = pd.read_csv(data_frame)
        self.train = train

        if self.train == True:
            self.data = data.values[:, 1:-1440]
            #print("Train", self.data)

        else:
            self.data = data.values[:, -1440:]
            #print("Test", self.data)

    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, index):
        x = self.data[index, index : index + 336].reshape(7, 48)
        y = self.data[index, index + 336 : index + 336 + 48].reshape(1, 48)
        return x, y


if __name__ == "__main__":
    train_dataset = TSData('/daintlab/data/CER_electricity/new_data.csv', train=True)
    test_dataset = TSData('/daintlab/data/CER_electricity/new_data.csv', train=False)
    
    train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    for x,y in enumerate(train_dataloader):
        print(x)
        print(y)

    