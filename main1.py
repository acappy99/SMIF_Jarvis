import sys
from time import sleep
import numpy as np
import pandas as pd
import datetime
import pickle
import matplotlib.pyplot as plt
import mgmt

# constant variables
report_path = '/Users/alexcappadona/Desktop/JARVIS/report/data.xlsx'
aaa_path = '/Users/alexcappadona/Desktop/JARVIS/aaa/'
asset_hist_path = '/Users/alexcappadona/Desktop/JARVIS/asset_hist/'

# fun intro
#words = "Welcome to SMIF_Jarvis\n"
#for char in words:
#    sleep(0.1)
#    print(char, end='', flush=True)
#print('')

print('0 - Exit')
print('1 - Add new asset detail')
print('2 - Review Portfolio')
print('')

# User input with data validation
while True:
    try:
        selection = int(input('Enter selection >'))
        break
    except ValueError:
        print('Error, please enter an integer')

if selection == 1:
    # 1: saves the currently stored asset path as yesterday's
    yest_path = mgmt.get_ass_path()
    mgmt.save_yest_path(yest_path)

    # 2: takes new info and retrieves data
    print('')
    fname = input('Input filename: ')
    date = input('Report date (yyyy-mm-dd): ')
    loc = aaa_path+fname
    ass = pd.read_excel(loc)
    assets = mgmt.get_assets(ass)
    mgmt.save_asset_frame(assets, asset_hist_path, date)

    #3. replaces asset path with latest info
    loc = asset_hist_path+date+'_assets.xlsx'
    mgmt.save_ass_path(loc)
    curr_aum = mgmt.port_aum(assets, date)
    mgmt.update_aum(curr_aum)

if selection == 2:
    print('')
    today = str(datetime.date.today())
    xlsx = pd.ExcelFile(mgmt.get_ass_path())
    assets = pd.read_excel(xlsx)
    curr_aum = mgmt.port_aum(assets, today)


words = "Asset detail...\n"
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)

print(assets)

print('')
input('<Press enter to continue>')
print('')

aum_frame = mgmt.get_aum_record()
print('Assets Under Management:')
print(aum_frame)
print('')

aum_chg = str(mgmt.aum_delta(aum_frame))
aum_pchg = str(mgmt.aum_delta_per(aum_frame))
print('One day change in portfolio AUM:')
print('$'+aum_chg)
print(aum_pchg+'%')

words = "Generating AUM chart\n\n"
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)

mgmt.aum_graph(aum_frame)


print('0 - Exit')
print('1 - Generate Report')
print('')

# User input with data validation
while True:
    try:
        selection = int(input('Enter selection >'))
        break
    except ValueError:
        print('Error, please enter an integer')

if selection == 1:
    securities = mgmt.drop_non_sec(assets)
    print(securities)
    #mgmt.gen_report(report_path, assets, securities, aum_frame)
    
    words = "Generating report...\n"
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)
    
    mgmt.gen_report(report_path, assets, securities, aum_frame)
    print('Success')

words = "Goodbye\n"
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)