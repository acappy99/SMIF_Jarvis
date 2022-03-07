import numpy as np
import pandas as pd
import datetime as datetime
import pickle
import matplotlib.pyplot as plt
import mgmt

path = input('Path: ')
fname = input('Filename: ')
loc = path+fname

# total portfolio dataframe
ass = pd.read_excel(loc)

# assets, base cost, market cost dataframe
assets = mgmt.get_assets(ass)
print(assets)

# AUM dataframe
print('')
aum = mgmt.port_aum(assets)
print('Current period assets under management:')
print(aum)
print('')

# Record current pd AUM in record, takes aum dataframe
# Records with date as current date from datetime()
print('writing to AUM history...')
mgmt.record_aum(aum)
print('')

# Show AUM history
print('')
aum_record = mgmt.get_aum_record()
print('AUM History')
print(aum_record)
print('')

# create DataFrame of only securities
print('Fields to drop, separated by enter, type "done" when finished.')
drop_lst = []
while True:
    drops = input('>')
    if drops == 'done':
        break
    drops = int(drops)
    drop_lst.append(drops)
securities = mgmt.drop_fields(assets, drop_lst)
print(securities)

