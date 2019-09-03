import pandas as pa

data = pa.read_csv("HR.csv")

print(data)

data.pop('Hire Date')      # POP Hire Data Column from the file

print(data)