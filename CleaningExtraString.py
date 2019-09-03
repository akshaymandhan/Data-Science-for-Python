import pandas as pd

df = pd.read_csv('C:\\Users\\ACER\\Desktop\\Akshay Szabist\\Semester 8\\Data Science\\Python Files\\Book.csv')

# Book.csv ek bari file hai sari data show nh hoti, is liye ye code likhna zaruri hai.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print(df.head(8))

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(extr.loc[206:].head(5))

#  this will remove first four string which we dont want in date of publication from row 206