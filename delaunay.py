import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

vertices = np.array([[200, 180], [180, 190], [165, 210], [165, 235], [150,              # Enter custom vertices to triangulate
250], [100, 170], [120, 120], [150, 100], [170, 140], [130, 150]])

tri = Delaunay(vertices)

plt.triplot(vertices[:,0], vertices[:,1], tri.simplices)
plt.plot(vertices[:,0], vertices[:,1], 'o')
plt.show()