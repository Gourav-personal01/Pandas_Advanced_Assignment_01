# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.

# Solution - 

import pandas as pd
df = pd.DataFrame({
    "Values" : [1,2,3,4,5,6]
})

mean_of_values = df['Values'].mean()
print(mean_of_values)

meadian_of_values = df['Values'].median()
print(meadian_of_values)

standard_deviation_of_values = df['Values'].std()
print(standard_deviation_of_values)