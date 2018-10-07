%matplotlib notebook
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

fig = plt.figure()
fig.add_subplot(1,1,1)
fig.scatter(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()

fig3d = plt.figure()
ax = fig3d.add_subplot(projection="3d")
constellation3d = ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
