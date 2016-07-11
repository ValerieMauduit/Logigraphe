import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#x = np.array([[1, 0, 0, 0, 1], [0, 2, 0, 2, 0], [0, 0, 3, 0, 0], 
#    [0, 4, 4, 4, 0], [5, 5, 5, 5, 5]])
#fig, ax = plt.subplots()
#ax.imshow(x, cmap = cm.gray_r, interpolation='nearest')
#plt.show()

# Copie exemple Internet
#----------------------------------------------------
def hinton(matrix, max_weight=None, ax=None):
    """Draw Hinton diagram for visualizing a weight matrix."""
    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2**np.ceil(np.log(np.abs(matrix).max())/np.log(2))
    matrix = matrix * 1.0 / max_weight

    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x, y), w in np.ndenumerate(matrix):
        color = 'white' if w > 0 else 'black'
        size = np.sqrt(np.abs(w))
        rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()
#----------------------------------------------------

# La fonction d'animation... Voir comment l'intégrer
#----------------------------------------------------
x = x + 1 
for (l, c), w in np.ndenumerate(x):
     if w < -9:
         x[l][c] = 9

#----------------------------------------------------

# Initialisations et lancement
#----------------------------------------------------
n = 10
x = np.array([[x - y for x in range(n)] for y in range(n)])
hinton(x, max_weight = 9)
plt.show()
#----------------------------------------------------

