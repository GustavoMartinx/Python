import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a Specific Element [l, c]
print(a[1, 5])

# Get a Specific Row
print(a[0, :])

# Get a Specific Column
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize] [inicio:fim:pulo]
print(a[0, 1:-1:2])

a[1,5] = 20
print(a)

a[:,2] = [1,2]
print(a)


## 3D Example ##
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)

# Get Specific Element (work outside in)
print(b[0,1,1])

# Replace
b[:,1,:] = [[9,9], [8,8]]
print(b)
