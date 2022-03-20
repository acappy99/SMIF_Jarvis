# sandbox
import sys
from time import sleep
import numpy as np
import pandas as pd
import datetime as datetime
import pickle
import matplotlib.pyplot as plt
import mgmt
import buys_sells

asset_hist_path = '/Users/alexcappadona/Desktop/JARVIS/asset_hist/'
aaa_path = '/Users/alexcappadona/Desktop/JARVIS/aaa/'
asset_hist_path = '/Users/alexcappadona/Desktop/JARVIS/asset_hist/'

#words = "Entering sandbox...\n"
#for char in words:
 #   sleep(0.1)
 #   print(char, end='', flush=True)

# Old date for testing
test_file = '2022-03-07_assets.xlsx'
yest_assets = pd.read_excel(asset_hist_path+test_file)

# Today
today_path = mgmt.get_ass_path()
today_assets = pd.read_excel(today_path)

yest_sec = mgmt.drop_non_sec(yest_assets)
today_sec = mgmt.drop_non_sec(today_assets)

yest_sec = yest_sec.set_index('Ticker')
today_sec = today_sec.set_index('Ticker')

# create security lists
yest_tick = yest_sec.index.values.tolist()
today_tick = today_sec.index.values.tolist()

# complete sell list
sell_lst = []
for i in yest_tick:
    if i not in today_tick:
        sell_lst.append(i)

# new purhcases list
buy_lst = []
for i in today_tick:
    if i not in yest_tick:
        buy_lst.append(i)

print('')
# output
if buy_lst == []:
    print('No new securities purchased over period','\n')
else:
    print('New securities purchased:\n',buy_lst,'\n')

if sell_lst == []:
    print('No securties sold over period','\n')
else:
    print('Security positions completely sold:\n',sell_lst,'\n')

print('')
input('<Enter to continue>')

### security price changes

# create list of today's tickers and prices
today_p = {}
for i in today_tick:
    price = today_sec.at[i,'Base Market Value']
    today_p[i] = price
# create list of today's tickers and yesterday's prices
yest_p = {}
for i in today_tick:
    if i not in sell_lst:
        price = yest_sec.at[i,'Base Market Value']
        yest_p[i] = price

p_sum = pd.DataFrame({'Previous Price':pd.Series(yest_p),'Current Price':pd.Series(today_p)})

p_sum['Change'] = p_sum['Current Price'] - p_sum['Previous Price']

pchange = p_sum['Change'].to_dict()

pos_pchange = {}
neg_pchange = {}

for tick in pchange:
    if pchange[tick] > 0:
        pos_pchange[tick] = pchange[tick]

for tick in pchange:
    if pchange[tick] < 0:
        neg_pchange[tick] = pchange[tick]

#print('Gainers\n',pos_pchange)
#print('Losers\n',neg_pchange)

### Get top 5 and bottom 5

# Postive list
x = 0
for i in pos_pchange:
    if pos_pchange[i] > x:
        x = pos_pchange[i]




x = 0
for i in neg_pchange:
    if neg_pchange[i] < 0:
        x = neg_pchange[i]

print(x)