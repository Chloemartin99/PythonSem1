import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

#create an incremental list of dates
dates = pd.date_range('20191101', periods=7)
print("Dates List")
print(dates)

#create a data frame
#28 random values (displayed in 7*4) in a table indexed by the dates that we created, the column names are A, B, C & D
#common for stock value data (due to the date in the index)
print("")
print("")
print("The data")
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
print(df)

#auto completion
print("")
print("")
print("Auto Completion")
print(df.A) #only the column A

#stats
print("")
print("")
print("Stats")
print(df.describe())

#selection (by column and row
#get column C
print("")
print("")
print("Selection of column C")
print(df["C"])

#get column B and C, rows 2 and 3
print("")
print("Selection of columns B and C, rows 2 and 3")
print(df.loc[[dates[2], dates[3]], ["B", "C"]])

#change a value
print("")
print("")
print("Change a value")
df.loc[dates[3], ["B"]] = 7777
print(df)

#selection by position
print("")
print("")
print("Selection by position")