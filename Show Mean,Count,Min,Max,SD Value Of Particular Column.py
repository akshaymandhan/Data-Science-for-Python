import pandas as pa


data = pa.read_csv("efile_2.csv")

#print(data)

print('Mean=', data.Salary.mean(), '\nCount=', data.Salary.count(), '\nMin Salary=', data.Salary.min(), '\nMax Salary=', data.Salary.max(),'\nSD=', data.Salary.std())

print(data.columns)        # Show Columns Heading


