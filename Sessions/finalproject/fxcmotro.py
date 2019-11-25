import fxcmpy
import pandas as pd
import datetime as dt
TOKEN="c9828dd51da672e51cf4afcb8d51b625a2fefea3"
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo')
con.subscribe_market_data('EUR/USD')
con.get_candles('EUR/USD', period='m1', number=10)

df = con.get_candles('GBP/USD', period='D1',start= dt.datetime(2016, 1, 1),end = dt.datetime(2018, 6, 10))
df.reset_index(inplace=True)
df.date= df.date.dt.tz_localize('US/Eastern').dt.tz_convert('Europe/Dublin')