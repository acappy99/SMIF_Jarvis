import numpy as np
import pandas as pd
from datetime import datetime
import pickle

# takes DataFrame of portfolio data
# creating new DataFrame with security, base cost, and market value for all assets
def get_assets(ass):
    asset_name = pd.DataFrame(ass['Security Description 1'])
    base_price = pd.DataFrame(ass['Base Cost'])
    market_price = pd.DataFrame(ass['Base Market Value'])
    frames = [asset_name,base_price,market_price]
    result = pd.concat(frames, axis=1)
    return result

# takes a dataframe of portfolio assets
# returns a dataframe without non-security assets/liabilities
def drop_fields(ass_frame, drop_lst):
    sec_lst = ass_frame.drop(drop_lst)
    return sec_lst

# takes dataframe of portfolio assets
# returns DataFrame with the current date and assets under management
def port_aum(ass_frame):
    base_mv = ass_frame['Base Market Value'].tolist()
    aum = sum(base_mv)
    today = datetime.today().strftime('%Y-%m-%d')
    entry = {"AUM": pd.Series(aum, index=[today])}
    aum = pd.DataFrame(entry)
    return aum

def record_aum(new_entry):
    rfile = open("aum.pickle","rb")
    aum_data = pickle.load(rfile)
    aum_record = pd.concat([aum_data,new_entry])
    wfile = open("aum.pickle","wb")
    pickle.dump(aum_record,wfile)
    return aum_record

# takes no arugments
# checks what is saved in aum.pickle
def get_aum_record():
    rfile = open("aum.pickle","rb")
    aum_data = pickle.load(rfile)
    return aum_data

# takes a date, file
# drops the date in file
def drop_date(date,file):
    rfile = open(file,"rb")
    aum_data = pickle.load(rfile)
    new_aum_data = aum_data.drop(labels=[date])
    wfile = open(file,"wb")
    pickle.dump(new_aum_data,wfile)
    return

# takes aum_frame
# returns one day price change in aum
def aum_delta(aum_frame):
    aum_lst = aum_frame['AUM'].tolist()
    periods = len(aum_lst)
    current_pd = int(periods - 1)
    last_pd = int(periods - 2)
    delta = round((aum_lst[current_pd] - aum_lst[last_pd]),2)
    return delta

# takes aum_frame
# returns one day percent change in aum
def aum_delta_per(aum_frame):
    aum_lst = aum_frame['AUM'].tolist()
    periods = len(aum_lst)
    current_pd = int(periods - 1)
    last_pd = int(periods - 2)
    delta_per = (aum_lst[current_pd]/aum_lst[last_pd])-1
    return delta_per