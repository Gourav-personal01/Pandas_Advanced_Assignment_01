# Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# Solution - 

import pandas as pd

data1 = pd.date_range(start='2023-01-01',end = '2023-01-31')

df = pd.DataFrame({
    "Date" : data1
})

print(df)
