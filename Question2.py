# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
#     DataFrame with a new index that starts from 1 and increments by 2 for each row.

# Solutions - 
import pandas as pd

df = pd.DataFrame({
    "A" : [1,2,3,4,5,6,7],
    "B" : [5,6,7,8,1,2,3],
    "C" : [2,3,6,7,2,2,2],
},index=['1','3','5','7','9','11','13'])
print(df)