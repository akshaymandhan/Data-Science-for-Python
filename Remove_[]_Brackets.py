import pandas as pa

data = pa.read_csv("Book.csv")

pa.set_option('display.max_rows', 500)
pa.set_option('display.max_columns', 500)
pa.set_option('display.width', 1000)

extr = data['Date of Publication'].str.extract(r'^(\d{4})', expand=False)  # Remove [] from the define column
print(extr.loc[206:].head(8))
