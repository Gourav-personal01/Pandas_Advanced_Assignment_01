# You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.
# The username is the part of the email address that appears before the '@' symbol. For example, if the
# email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your
# function should extract the username from each email address and store it in the new 'Username'
# column.

import pandas as pd 

df = pd.DataFrame({
    "Email" : ["gouravkumar@domain.com","subhashkumar@domain.com"]
})

print(df)

df['Username'] = df['Email'].apply(lambda x : x.removesuffix("@domain.com"))

print(df)
