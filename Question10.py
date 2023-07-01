# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

# Solution - 

import pandas as pd
df = pd.DataFrame({
    "Sales" : [199,299,399,499,599,699,799,899],
    "Date"  : ["2023-06-20","2023-06-21","2023-06-22","2023-06-23","2023-06-24","2023-06-25","2023-06-26","2023-06-27"]
    })

print(df)

df['MovingAverage'] = df['Sales'].rolling(window=7).mean()
print(df)