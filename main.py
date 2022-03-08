import sys
from time import sleep
import numpy as np
import pandas as pd
import datetime as datetime
import pickle
import matplotlib.pyplot as plt
import mgmt

# constant variables
report_path = '/Users/alexcappadona/Desktop/JARVIS/output/data.xlsx'
aaa_path = '/Users/alexcappadona/Desktop/JARVIS/aaa/'

# fun intro
words = "Welcome to SMIF_Jarvis\n"
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)

# Additions:
#   * User option to add new file
#   * Save current report as "today's report"
#   * Save old "today's report" as yesterday's report
#   * Check for bought or sold securuties by comparing today's and yesterday's reports

print('')
print('Asset and accrual')
fname = input('Filename: ')
loc = aaa_path+fname

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
print('Add current AUM to history? (y/n)')
selection = input('>')
if selection == 'y':
    words = "Writing to AUM history...\n"
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)
    mgmt.update_aum(aum)
    print('')

# Show AUM history
print('')
aum_frame = mgmt.get_aum_record()
print('AUM History')
print(aum_frame)
print('')

# AUM delta $
print('One day ($) change in AUM:')
aum_delta = mgmt.aum_delta(aum_frame)
print(aum_delta)
print('')

# AUM delta %
print('One day (%) change in AUM:')
aum_delta_per = mgmt.aum_delta_per(aum_frame)
print(aum_delta_per)
print('')

# AUM graph
print('View AUM chart? (y/n)')
selection = input('>')
print('')
if selection == 'y':
    words = "Creating AUM chart...\n"
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)
    mgmt.aum_graph(aum_frame)

# Create DataFrame of only securities
securities = mgmt.drop_non_sec(assets)
print(securities)

print('')
print('Generate report? (y/n)')
selection = input('>')
if selection == 'y':
    words = "Generating report...\n"
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)
    mgmt.gen_report(report_path, assets, securities, aum_frame)
    print('Success. Output save at: '+report_path)