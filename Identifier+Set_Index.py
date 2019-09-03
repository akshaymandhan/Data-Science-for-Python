import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('D:\\Aakash\\Szabist\\Semester 8\\Data Science\\Data\Book.csv')

# Book.csv ek bari file hai sari data show nh hoti, is liye ye code likhna zaruri hai.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# this will return boolean if result is unique
print(df['Identifier'].is_unique)


# this will remove the "Job Id" column and start with col of given value
df = df.set_index('Identifier')

# print data 5 rows
print(df.head())