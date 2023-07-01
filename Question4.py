#Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
#'Word_Count' that contains the number of words in each row of the 'Text' column.

import pandas as pd

df = pd.DataFrame({
    "Text" : ["My Name is Gourav and I'm intested to learn python"]
})

df['Word_Count'] = df['Text'].apply(lambda x : len(x.split()))

print(df)