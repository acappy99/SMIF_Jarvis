import numpy as np
import pandas as pd
from datetime import datetime
import pickle
import matplotlib.pyplot as plt

# takes DataFrame of portfolio data
# creating new DataFrame with security, base cost, and market value for all assets
def get_assets(ass):
    ticker = pd.DataFrame(ass['Ticker'])
    asset_name = pd.DataFrame(ass['Security Description 1'])
    shares_par = pd.DataFrame(ass['Shares/Par'])
    base_price = pd.DataFrame(ass['Base Cost'])
    market_price = pd.DataFrame(ass['Base Market Value'])
    frames = [ticker,asset_name,shares_par,base_price,market_price]
    result = pd.concat(frames, axis=1)
    return result

# takes most recent asset_frame, save path, and as of data date
# saves in asset_hist
def save_asset_frame(asset_frame, asset_hist_path, date):
    file_path = asset_hist_path+date+'_assets.xlsx'
    asset_frame.to_excel(file_path)
    return file_path

# save asset_frame path to be opened later
def save_ass_path(loc):
    wfile = open("asspath.pickle","wb")
    loc = loc
    pickle.dump(loc,wfile)

def get_ass_path():
    rfile = open("asspath.pickle","rb")
    assets = pickle.load(rfile)
    return assets

def save_yest_path(loc):
    wfile = open("yestasspath.pickle","wb")
    loc = loc
    pickle.dump(loc,wfile)

# takes a dataframe of portfolio assets
# returns a dataframe without non-security assets/liabilities
def drop_non_sec(ass_frame):
    sec_frame = ass_frame.dropna(subset=["Ticker"])
    return sec_frame

# takes dataframe of portfolio assets
# returns DataFrame with the current date and assets under management
def port_aum(ass_frame):
    base_mkt_val = ass_frame['Base Market Value']
    aum = round(base_mkt_val.sum(),2)
    today = datetime.today().strftime('%Y-%m-%d')
    entry = {"AUM": pd.Series(aum, index=[today])}
    aum = pd.DataFrame(entry)
    return aum

# to override date
def port_aum1(ass_frame,date):
    base_mkt_val = ass_frame['Base Market Value']
    aum = round(base_mkt_val.sum(),2)
    entry = {"AUM": pd.Series(aum, index=[date])}
    aum = pd.DataFrame(entry)
    return aum

# update the aum pickle
def update_aum(new_entry):
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

# for maintenance purposes takes a date, file
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
    delta_per = round((aum_lst[current_pd]/aum_lst[last_pd])-1,2)
    return delta_per

# takes aum_frame
def aum_graph(aum_frame):
    plt.figure(1)
    plt.plot(aum_frame['AUM'], label='AUM')
    plt.xlabel('Date')
    plt.ylabel('AUM')
    plt.title('AUM History')
    plt.grid(True)
    plt.legend()
    return plt.show()

# takes three DataFrames
# creates report in the main file's designated path
def gen_report(report_path, ass_frame, sec_frame, aum_frame):
    with pd.ExcelWriter(report_path) as writer:
        ass_frame.to_excel(writer, sheet_name='Assets')
        sec_frame.to_excel(writer, sheet_name='Securities')
        aum_frame.to_excel(writer, sheet_name='AUM_History')
    return