import numpy as np
import matplotlib.pyplot as plt

# 1-D array of ints
a = np.array([1,2,3])
print(a)
a.ndim
a.shape

# 2-D array of floats — in this case, a list within a list
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
b.ndim
b.shape

# 3-D array of ints — three lists inside a list
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)
c.ndim
c.shape

# get type and size of arrays
a.dtype

# get size
a.itemsize

# get total size (nbytes = itemsize * size)
a.nbytes

Accessing and changes specific elements, rows, cols, etc.

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# get specific element [r, c] (recall it uses 0-indexing) (can use negative indexing like in lists {-1 gets the last element, for example})
a[1, 5]


# get a specific row (the first one) // a[0] also works
a[0, :]

# get a spefici col
a[:, 2]

# [startindex:endindex:stepsize]
a[0, 1:6:2]

a[:, 2] = 99
a

3-D example

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

# get specific element (work ouside in — look for the 4) (so target the first set, then the row, then the col)
b[0,1,1]

# get the first row from both arrays (:,0,: means "all dimensions, first row, all cols" in the DRC framework)
b[:,0,:]

# get the second row from both arrays
b[:,1,:]

# replace a specific element (in this case, the 6)
b[1,0,1] = 99
print(b)
