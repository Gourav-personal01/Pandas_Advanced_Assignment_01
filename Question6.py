# Q6. Which function of pandas do we use to read an excel file?

# Solution - 

# pd.read_excel is used to read an excel file

import pandas as pd

df1 = pd.read_excel("LUSID Excel - Setting up your market data.xlsx")
print(df1)