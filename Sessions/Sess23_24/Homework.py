from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("CocaCola.csv")
df1['Date'] = pd.to_datetime(df1.Date)

df2 = pd.read_csv("Nestle.csv")
df2['Date'] = pd.to_datetime(df2.Date)

df3 = pd.read_csv("Pepsi.csv")
df3['Date'] = pd.to_datetime(df3.Date)

plt.style.use('seaborn-darkgrid')
palette = plt.get_cmap('Set1')


plt.figure("Coca Cola")
plt.plot(df1["Date"], df1["Close"], marker = '', color = palette(2), linewidth=1, alpha=0.9, label="Coca Cola")
plt.plot(df2["Date"], df2["Close"], marker = '', color = palette(3), linewidth=1, alpha=0.9, label="Nestle")
plt.plot(df3["Date"], df3["Close"], marker = '', color = palette(4), linewidth=1, alpha=0.9, label="Pepsi")

plt.xlabel("Dates", fontsize=12)
plt.ylabel("Stock Value (USD)", fontsize=12)
plt.legend(loc='left', ncol=2)
plt.title('Stock Prices from 2000 to end of 2018 of Coca Cola, Nestle & Pepsi',
          loc = 'center', fontsize=13, fontweight=0, color='black')

plt.show()