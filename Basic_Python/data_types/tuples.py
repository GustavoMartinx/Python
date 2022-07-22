names = ('Mari', 'Gu', 'Bia', 'Ana')
print(type(names))
print(names)

print('Mari' in names) # True
print('gu' in names)   # False (letra minuscula, ou seja, um elem que nao existe em names)

print(names[0])
print(names[1:2])  # Print de 1 até 2, sem imprimir o 2
print(names[1:-1]) # da posicao 1 até -1, sem imprimir o -1
print(names[1:])   # da posicao 1 ate o fim
print(names[:-2])  # até os dois últimos, sem imprimir os dois últimos

print(f'{names[0]} and {names[1]}, the best couple of the world!')
