import pandas as pd
from datetime import datetime

RT = pd.read_csv('sensor_IOT.csv')
RT['TS'] = pd.to_datetime(RT['TS'])
TSF = RT['TS'].iloc[:1]
TSL = RT['TS'].iloc[-1:]
TT = pd.to_timedelta(TSL.values[0]-TSF.values[0])
print(TT)
