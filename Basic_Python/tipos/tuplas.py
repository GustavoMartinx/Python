nomes = ('Mari', 'Gu', 'Bia', 'Ana')
print(type(nomes))
print(nomes)

print('Mari' in nomes) # True
print('gu' in nomes)   # False (letra minuscula, ou seja, um elem que nao existe em nomes)

print(nomes[0])
print(nomes[1:2])  # Print de de 1 até 2, sem imprimir o 2
print(nomes[1:-1]) # da posicao 1 até -1, sem imprimir o -1
print(nomes[1:])   # da posicao 1 ate o fim
print(nomes[:-2])  # até os dois últimos, sem imprimir os dois últimos

print(f'{nomes[0]} e {nomes[1]}, o casal mais foda do mundo!')
