# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# For example, if df contains the following values:
#   A B C
# 0 3 5 1
# 1 8 2 7
# 2 6 9 4
# 3 2 3 5
# 4 9 1 2

# Your function should select the following rows: A B C
# 1 8 2 7
# 4 9 1 2
# The function should return a new DataFrame that contains only the selected rows.

# Solution - 

import pandas as pd
df = pd.DataFrame({
    'A' : [3,8,6,2,9],
    'B' : [5,2,9,3,1],
    'C' : [1,7,4,5,2]
})

df = df[(df['A'] > 5) & (df['B'] < 10)]
print(df)