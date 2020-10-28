import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


ts_data = pd.read_csv("/daintlab/data/CER_electricity/new_data.csv")

series_ts = pd.date_range('2009-07-14 00:00', '2010-12-31 23:30', periods=25728)
list_ts = ['ID']

for ts in series_ts:
    list_ts.append(ts)

ts_data = ts_data.T
ts_data['date_time'] = list_ts
ts_data.set_index('date_time', inplace=True)

ts_data = ts_data.T
ts_data = ts_data.drop('ID', axis=1)

plt.figure(figsize=(90, 5))
plt.plot(ts_data.iloc[1,:])
#plt.savefig('/daintlab/home/hojune/ts_git/plots/user1_all.png')

plt.figure(figsize=(30, 5))
plt.plot(ts_data.iloc[1,0:47])
#plt.savefig('/daintlab/home/hojune/ts_git/plots/user1_day1.png')

plt.figure(figsize=(30, 5))
plt.plot(ts_data.iloc[1,48:95])
#plt.savefig('/daintlab/home/hojune/ts_git/plots/user1_day2.png')