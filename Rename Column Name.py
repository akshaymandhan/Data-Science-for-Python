
import pandas as pa

data = pa.read_csv("HR.csv")

print(data)

print(data.rename(columns={'Min Salary': 'Min_Salary', 'Max Salary': 'Max_Salary'}))
