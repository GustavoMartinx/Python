a = 'valor' # True
a = 0 # True
a = -0.0001 # True
a = ''  # False
a = ' ' # False
a = []  # False
a = {}  # False

if a:
    print('Existe!')
else:
    print('nao existe ou eh zero ou vazio.')
