import pandas as pa

data = pa.read_csv("Book.csv")

print(data.loc[206:216])          # Print Rows From 206 to 216