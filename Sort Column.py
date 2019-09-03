import pandas as pa
import numpy as np

data = pa.read_csv("efile_2.csv")


print(data.sort_values(['Salary']))
