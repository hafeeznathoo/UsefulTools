'''
Data cleaning script

takes in df and returns a cleaned version

'''

import pandas as pd
import datetime as dt
import numpy as np

def MakeDate(df,yearcol,monthcol,daycol,timecol=None):
    '''
    takes in year, month, day series as floats
    
    and a time column as a time object, then combines them both to get a datetime
    '''
    year=df[yearcol]
    month=df[monthcol]
    day=df[daycol]
    df['temp_date']=(year*10000+month*100+day)
    df.temp_date=df['temp_date'].apply(lambda v: str(v) if str(v) != 'nan' else np.nan)
    df['temp_date'] = pd.to_datetime(df['temp_date'],format='%Y%m%d', errors='coerce')

    if timecol==None:
        return df['temp_date']
    else:
        return df.apply(lambda r: CombineTime(r['temp_date'].date(),r[timecol]),axis=1)
        
def Str2date(val):
    if pd.isna(val):
        val=np.nan
    else:
        val=str(int(val))      
    try:
        return dt.datetime.strptime(val, '%Y%m%d').date()
    except:
        return pd.NaT


def Str2time(val):

    try:
        return dt.datetime.strptime(val, '%H:%M:%S').time()
    except:
        return pd.NaT

def CombineTime(date,time):
    if pd.isnull(date) or pd.isnull(time):
        return pd.NaT
    try:
        return dt.datetime.combine(date,time)
    except:
        return pd.NaT

