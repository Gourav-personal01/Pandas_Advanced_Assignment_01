# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.

# For example, if df contains the following values:
# Date
# 0 2023-01-01
# 1 2023-01-02
# 2 2023-01-03
# 3 2023-01-04
# 4 2023-01-05
# Your function should create the following DataFrame:

# Date Weekday
# 0 2023-01-01 Sunday
# 1 2023-01-02 Monday
# 2 2023-01-03 Tuesday
# 3 2023-01-04 Wednesday
# 4 2023-01-05 Thursday
# The function should return the modified DataFrame.

# Solution - 

import pandas as pd 

date =pd.date_range(start='2023-01-01',end='2023-01-05')

df = pd.DataFrame({
    "Date" : date
})

df['Weekday'] = df['Date'].dt.day_name()

print(df)