import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x = np.array([[1, 0, 0, 0, 1], [0, 2, 0, 2, 0], [0, 0, 3, 0, 0], 
    [0, 4, 4, 4, 0], [5, 5, 5, 5, 5]])
fig, ax = plt.subplots()
ax.imshow(x, cmap = cm.gray_r, interpolation='nearest')
plt.show()
