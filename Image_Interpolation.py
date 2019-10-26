#==================================================================
#-----------------      Image Interpolation      ------------------
#==================================================================
# Pattern 1 : Basic Image in Python
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
plt.savefig("Besic_Python_Image.png", dpi=300)
plt.show()
plt.close()

#==================================================================
# Pattern 2 : Interpolation Image in BiLinear method
#------------------------------------------------------------------
# The BiLinear method is an interpolation method that 
# expands the Linear method variables into two dimensions.
#==================================================================

from scipy.interpolate import interp2d

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = np.cos(10*(x**2 + y**2)) * np.sin(10*(x**2 + y**2))

tck = interp2d(x, y, z, kind="linear")

xnew, ynew = np.mgrid[-1:1:200j, -1:1:200j]
znew = tck(xnew[:, 0], ynew[0, :])

plt.figure()
plt.pcolor(xnew, ynew, znew, cmap="jet")
plt.colorbar()
plt.savefig("BiLinear_Image.png", dpi=300)
plt.show()
plt.close()

#==================================================================
# Pattern 3 : Interpolation Image in BiCubic method
#==================================================================

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = np.cos(10*(x**2 + y**2)) * np.sin(10*(x**2 + y**2))

tck = interp2d(x, y, z, kind="cubic")

xnew, ynew = np.mgrid[-1:1:200j, -1:1:200j]
znew = tck(xnew[:, 0], ynew[0, :])

plt.figure()
plt.pcolor(xnew, ynew, znew, cmap="jet")
plt.colorbar()
plt.savefig("BiCubic_Image.png", dpi=300)
plt.show()
plt.close()

