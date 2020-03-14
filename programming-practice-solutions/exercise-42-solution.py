# plotting from a CSV file
from matplotlib import pyplot as plt
import numpy as np

x,y = np.loadtxt("./example_data.csv", unpack= True, delimiter = ',')
print (x)
print (y)
plt.plot(x,y)
plt.title('numpy CSV chart')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()
