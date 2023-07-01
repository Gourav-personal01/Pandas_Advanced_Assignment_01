#Q1. List any five functions of the pandas library with execution.

# Solution - 
# Most Usefull five functions of the pandas library are head, tail, describe , loc, iloc

import pandas as pd 

df =  pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# 1. Head Function
Head_of_df = df.head(2)
print(Head_of_df)

# 2. Tail Function 
Tail_of_df = df.tail(2)
print(Tail_of_df)

# 3. Describe function
Describe_of_df = df.describe()
print(Describe_of_df)

# 4. loc Function
loc_of_df = df.loc[0:2,['PassengerId','Survived']]
print(loc_of_df)

# 5. Iloc Function
Iloc_of_df = df.iloc[0:2,[0,1]]
print(Iloc_of_df)