import pandas as pa
import numpy as np

data = pa.read_csv("efile_2.csv")


print(data.info())     # info about entries, datatypes

print(data['Salary'].describe(),"\n")         # Find mean , count, std, min, 25%, 50%, 70%, Max , DataType of Given Column


