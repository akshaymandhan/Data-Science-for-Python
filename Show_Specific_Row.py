import pandas as pa

data = pa.read_csv("Book.csv")

print(data.loc[206])          # Show Particular Row Data 206 is identity
