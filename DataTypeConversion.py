import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#  ek to parse ka way ye hai read k waqt Hire date ko String se Date format mn change kar diya FROM FILE
df = pd.read_csv('C:\\Users\\ACER\\Desktop\\Akshay Szabist\\Semester 8\\Data Science\\Python Files\\efile_2.csv', parse_dates=['Hire Date'])
print(df)


# dusra way ye hai within project you are conversion type.
print('----------------------------------')
s = "101010" #it's String
res = int(s)
print(res)
print(type(res))


print('----------------------------------')
s = 1 #it's Int
res = float(s)
print(res)
print(type(res))

print('----------------------------------')
s = 1 #it's Int
res = str(s)
print(res)
print(type(res))



#  is se hume specific column ka type pata lagega
# print('------------------------------')
# print(type(df['Salary'][0]))


