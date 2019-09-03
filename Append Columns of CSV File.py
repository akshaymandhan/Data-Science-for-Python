import pandas as pa

data = pa.read_csv("HR.csv")

print(data)

append = data['Min Salary'] + data['Max Salary']
print(append)