import pandas as pa

data = pa.read_csv("HR.csv", usecols=['Job Title','Max Salary'])

print(data.loc[0:5])