import numpy as np

a = np.array([1,2,3,4])

# Addition
# a += 2
print(a + 2)

# Subtraction
# a -= 2
print(a - 2)

# Multiplication
# a *= 2
print(a * 2)

# Division
# a /= 2
print(a / 2)

# Power
# a ** 2
print(a ** 2)

# Operations Between Arrays
b = np.array([1,0,1,0])
c = a + b
print(c)


# Take The Sin and Cos
d = np.sin(a)
print(d)

e = np.cos(a)
print(e)


# Linear Agebra
# Multiplication of Matrix
f = np.ones([2,3])
print(f)

g = np.full([3,2], 2)
print(g)

h = np.matmul(f, g)
print(h)

# Find The Determinat
i = np.identity(3)
print(np.linalg.det(i))

# Statistics
stats = np.array([[1,2,3], [4,5,6]])
print(stats)

# max
j = np.min(stats)
# min
k = np.max(stats)
# sum
l = np.sum(stats)

print(j)
print(k)
print(l)


# Reorganizing Arrays
before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)

# Vertically Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

v_stack_vec = np.vstack([v1,v2,v2])
print(v_stack_vec)

# Horizon Stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

h_stack_vec = np.hstack((h1,h2))
print(h_stack_vec)

# Load Data from File
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata.astype('int32')
print(filedata)

# Boolean Masking and Advanced Indexing
m = filedata > 50
print(m)

n = filedata[filedata > 50]
print(n)

# np.any(filedata > 50, axis=0)
# e np.all() q n entendi
