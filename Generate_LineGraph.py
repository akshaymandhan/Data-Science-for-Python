import pandas as pa
import numpy as np
import matplotlib.pyplot as plot

data = pa.read_csv("HR.csv")

plot.plot(data["Max Salary"])            # DEfine Column for the graph
plot.xlabel("Max Salary")                # Show Lable in the Graph for identification

plot.draw()                               # Draw Graph
plot.show()                               # Show Graph