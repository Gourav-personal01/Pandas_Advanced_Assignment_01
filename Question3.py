# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.

# Solution - 
import pandas as pd

df = pd.DataFrame({
    "Values" : [10,20,30,40,50]
})

first_three_values = df.head(3)
print(first_three_values)

Sum_of_first_three_values = first_three_values['Values'].sum()
print(Sum_of_first_three_values)
