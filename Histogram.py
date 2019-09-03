import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('D:\\Aakash\\Szabist\\Semester 8\\Data Science\\Data\HR.csv')


# print(df.columns)
# print(df.hist())

print(df['Min Salary'].hist())
plt.xlabel('Min Salary')
plt.draw()
plt.show()
