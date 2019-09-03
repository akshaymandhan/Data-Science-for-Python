import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Q: jis ka 4, 7, 10, 11 saal ka experience hai uski salary find karni hai via interpolation.

experiences = np.array([3, 6, 9, 12, 15])
salary = np.array([3000, 6000, 9000, 12000, 15000])


f = interpolate.interp1d(experiences, salary)
experiences_new = np.array([4, 7, 10, 11])
#salary4 = f(4)
print('--------------------')
plt.plot(experiences, salary, 'r-', experiences_new, f(experiences_new), 'bo')
plt.draw()
plt.show()
