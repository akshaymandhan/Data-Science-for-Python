import pandas as pa
import numpy as np

data = pa.read_csv("Book.csv")

data = data.set_index('Identifier')

print(data)