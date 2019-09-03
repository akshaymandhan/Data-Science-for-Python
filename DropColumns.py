import pandas as pa
import numpy as np

data = pa.read_csv("Book.csv")

pa.set_option('display.max_rows', 1000)            # Print max rows
pa.set_option('display.max_column', 1000)          # Print max columns
pa.set_option('display.width', 1000)               # Display data width

# Drop Below Define Columns from the Book.CSV File

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Issuance type',
           'Shelfmarks']
data.drop(columns=to_drop, inplace=True)

print(data)


