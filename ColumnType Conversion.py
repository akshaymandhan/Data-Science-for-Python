import pandas as pd

df = pd.read_csv('C:\\Users\\ACER\\Desktop\\Akshay Szabist\\Semester 8\\Data Science\\Python Files\\HR.csv')


print(df, "\n")


convert = df['Min Salary'].astype('float')
print(convert)




