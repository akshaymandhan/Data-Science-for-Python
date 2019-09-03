import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('Data\Book.csv')

# Book.csv ek bari file hai sari data show nh hoti, is liye ye code likhna zaruri hai.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

 # show specific row by LOC
print(df.loc[206])

