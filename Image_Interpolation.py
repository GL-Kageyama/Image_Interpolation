#==================================================================
#-----------------      Image Interpolation      ------------------
#==================================================================
#                        Basic Image 
#------------------------------------------------------------------
# Use the algorithm to create a dot picture before interpolation.
#==================================================================

import numpy as np
import matplotlib.pyplot as plt

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = np.cos(10*(x**2 + y**2)) * np.sin(10*(x**2 + y**2))

plt.figure()
plt.pcolor(x, y, z, cmap="jet")
plt.colorbar()
plt.savefig("Besic.png", dpi=300)
plt.show()
plt.close()

#==================================================================
#                      BiLinear method
#------------------------------------------------------------------
# The BiLinear method is an interpolation method that 
# expands the Linear method variables into two dimensions.
#==================================================================

from scipy.interpolate import interp2d

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = np.cos(10*(x**2 + y**2)) * np.sin(10*(x**2 + y**2))

# This is BiLinear method Point.
tck = interp2d(x, y, z, kind="linear")

xnew, ynew = np.mgrid[-1:1:200j, -1:1:200j]
znew = tck(xnew[:, 0], ynew[0, :])

plt.figure()
plt.pcolor(xnew, ynew, znew, cmap="jet")
plt.colorbar()
plt.savefig("BiLinear.png", dpi=300)
plt.show()
plt.close()

#==================================================================
#                       BiCubic method
#------------------------------------------------------------------
# The BiCubic method is an interpolation method that extends 
# the one-dimensional Cubic method.
#==================================================================

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = np.cos(10*(x**2 + y**2)) * np.sin(10*(x**2 + y**2))

# This is BiCubic method Point.
tck = interp2d(x, y, z, kind="cubic")

xnew, ynew = np.mgrid[-1:1:200j, -1:1:200j]
znew = tck(xnew[:, 0], ynew[0, :])

plt.figure()
plt.pcolor(xnew, ynew, znew, cmap="jet")
plt.colorbar()
plt.savefig("BiCubic.png", dpi=300)
plt.show()
plt.close()

