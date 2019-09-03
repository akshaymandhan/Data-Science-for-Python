import pandas as pa

data = pa.read_csv("Book.csv")

pa.set_option('display.max_rows', 500)
pa.set_option('display.max_columns', 500)
pa.set_option('display.width', 1000)

print(data)