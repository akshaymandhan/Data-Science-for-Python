import pandas as pa
import numpy as np
import matplotlib.pyplot as plot
from scipy import interpolate
import csv
import seabornas as sns



print('------------------- Read Complete File Through Pandas -------------------------')

data = pa.read_csv('HR.csv')
print(data, "\n")

print('--------------- Read Particular Columns Through Pandas --------------------------')

data = pa.read_csv('HR.csv', usecols=['Min Salary' , 'Max Salary'])
print(data, "\n")

print('---------------------- Read File Through CSV -----------------------')

with open('HR.csv')as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row, "\n")

print('---------------------- Read PArticular Columns of File Through CSV -----------------------')

with open('HR.csv')as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[0], row[1], "\n")

print('---- Show DataTypes of the Columns as dtypes , rows and columns as shape, how many ints string etc as info , mean median mode etc as describe -----')

data = pa.read_csv('HR.csv')
print(data.dtypes, "\n")
print(data.info(), "\n")
print(data.describe(), "\n")
print(data.shape, "\n")
print(data.head(), "\n")

print('----------------------- Show mean Count & SD of particular column ----------------------')

data = pa.read_csv("efile_2.csv")
print("Mean of Salary is", " ", data.Salary.mean(), "\n")
print("Count of Salary is", " ", data.Salary.count(), "\n")
print("SD of Salary is", " ", data.Salary.std(), "\n")

print('----------------- Show mean Count & SD of particular column in Single Line ---------------------')

print("\nMean of Salary is", " ", data.Salary.mean(), "\nCount of Salary is", " ", data.Salary.count(), "\nSD of Salary is", " ", data.Salary.std(), "\n")

print('----------------- POP Function hard Coded Data ---------------------')

list = ['Apply', 'Discard', 'Ignore', 'I Love You']
list.pop()
print(list, "\n")

print('----------------- Remove Function hard Coded Data ---------------------')

list = ['Apply', 'Discard', 'Ignore', 'I Love You']
list.remove('Ignore')
print(list, "\n")

print('----------------- Insert Function hard Coded Data ---------------------')

list = ['Apply', 'Discard', 'Ignore', 'I Love You']
list.insert(1, 'Leave')
print(list, "\n")

print('----------------- Append Function hard Coded Data Using DataFrame ---------------------')

list1 =pa.DataFrame(['I', 'Love'])
list2 =pa.DataFrame(['You', 'My', 'Baby'])
list3 = list1.append(list2, ignore_index=True)
print(list3, "\n")

print('----------------- Drop Column of Hire Date Must Write Inplace=True ---------------------')

data = pa.read_csv('HR.csv')
to_drop= ['Hire Date']
data.drop(columns=to_drop, inplace=True)
print(data, "\n")

print('----------------- Remove Index Column  ---------------------')

data = pa.read_csv('HR.csv')
print(data.set_index(['Job ID']), "\n")

print('----------------- Rename Column Name Max Salary into Max_Salary ---------------------')

data = pa.read_csv('HR.csv')
print(data.rename(columns={'Max Salary' : 'Max_Salary'}), "\n")

print('----------------- Check Unique Index ---------------------')

data = pa.read_csv('HR.csv')
print(data['Job Title'].is_unique)

print('----------------- Show Specific Row, Range Using LOC ---------------------')

data = pa.read_csv('HR.csv')
print(data.loc[5], "\n")
print(data.loc[0:4], "\n")

print('----------------- Remove Extra Index of Row 206  ---------------------')

dataBook = pa.read_csv("Book.csv")
extra = dataBook['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(extra.loc[206:].head(8), "\n")

print('----------------- Sorting on the behalf of Hire Date ---------------------')

data = pa.read_csv('HR.csv')
print(data.sort_values(['Hire Date']), "\n")

print('----------------- Type Conversion ---------------------')

data = pa.read_csv('HR.csv')
convert = data['Min Salary'].astype(float)
print(convert, "\n")

convert = data['Job Title']
print(str(convert), "\n")

print('----------------- Window Setting ---------------------')

dataBook = pa.read_csv("Book.csv")

pa.set_option('Display.max_rows', 500)
pa.set_option('Display.max_columns', 500)
pa.set_option('Display.width', 1000)
print(dataBook.head(), "\n")

print('----------------- Get File Columns in Array Using Numpy ---------------------')

data = pa.read_csv('HR.csv')
maxSalary = np.array(data['Max Salary'])
minSalary = np.array(data['Min Salary'])
print(maxSalary, "\n", minSalary, "\n")


print('----------------- Print Histogram ---------------------')
data = pa.read_csv('HR.csv')
print(data['Min Salary'].hist())
plot.draw()
plot.xlabel("Histogram of Min Salary")
plot.show()
print("\n")

print('----------------- Print Line Graph ---------------------')
data = pa.read_csv('HR.csv')
plot.plot(data['Min Salary'])
plot.draw()
plot.xlabel("Line Graph of Min Salary")
plot.show()
print("\n")


print('----------------- Interpolation ---------------------')

exprince = np.array([1, 3, 5])
salary = np.array([4000, 6000, 8000])
result = interpolate.interp1d(exprince, salary)
new_exprience = np.array([2, 4])
plot.plot(exprince, salary, 'ro', new_exprience , result(new_exprience),'bo')
plot.draw()
plot.xlabel("Interpolation")
plot.show()
print("\n")


data=pa.read_csv('HR.csv')

sns.distplot(data['Min Salary'])
plot.draw()
plot.show()

