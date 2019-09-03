import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('HR.csv')

plt.plot(df['Min Salary'])
plt.xlabel('Min Salary')
plt.plot(df['Max Salary'])
plt.ylabel('Max Salary')

plt.draw()
plt.show()



append = df['Min Salary'] + df['Max Salary']
print(append)