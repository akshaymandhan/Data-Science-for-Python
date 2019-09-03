import pandas as pa
import numpy as np
import matplotlib.pyplot as plot


data = pa.read_csv("HR.csv")

print(data.columns)                           # Show Columns Names
print(data.hist(['Max Salary']))          # Generate Histogram of the integer columns
plot.draw()                                      # Draw the Grapg
plot.show()                                     # Show Graph
