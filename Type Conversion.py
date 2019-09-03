import pandas as pa

data = pa.read_csv("HR.csv", usecols=['Min Salary'])

print(data, "\n")


convert = data['Min Salary'].astype('float')
print(convert)




