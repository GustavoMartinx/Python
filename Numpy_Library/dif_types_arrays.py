import numpy as np

# All Zeros Matrix
print(np.zeros([4]))
print(np.zeros([2,3]))
print(np.zeros([2,3,2]))
print(np.zeros([2,3,3,2]))

# All Ones Matrix
print(np.ones([3,3]))
print(np.ones([3,3], dtype='int16'))

# Any Other Number
print(np.full([4,4], 82))

# Any Other Number (Full_like)
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(np.full_like(a, 4))
print(np.full(a.shape, 4))

# Random Decimal Numbers
print(np.random.rand(4,2,3))

# Random Integer Values
print(np.random.randint(7, size=(3,3)))

# The Identity Matrix
print(np.identity(3))

# Repeat
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# Output
output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)


# Copy
x = np.array([1,2,3])
y = x         # tanto o conteudo de x sera atribuido para y
y[0] = 100    # quanto a alteracao de um valor especifico em y sera tbm feita para x
print(x, y)

i = np.array([1,2,3])
j = i.copy()   # por outro lado, se usarmos a funao copy, a matriz i não é alterada quando mudamos algo em j
j[0] = 100
print(i, j)
