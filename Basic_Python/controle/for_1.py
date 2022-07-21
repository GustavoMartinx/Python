for i in range(10): # por padrao, de 0 até 10, excluindo o 10
    print(i)

for i in range(1, 11): # por padrao, de 1 até 11, excluindo o 11
    print(i)

for i in range(1, 100, 10): # de 1 até 100 de 10 em 10
    print(i)

nums = [2, 4, 6, 8]
for n in nums:
    print(n, end = ' ')  # imprime um espaco entre os elementos

texto = 'Python eh legal ate'
for letra in texto:
    print(letra, end = '')

for n in {1, 2, 3, 4, 4, 4}:
    print(n, end = ' ')


produto = {
    'nome': 'Caneta',
    'preco': 8.00,
    'desconto': 0.5
}

for atrib in produto:
    print(atrib, produto[atrib])

for atrib, valor in produto.items():
    print(atrib, valor)

for atrib in produto.values():
    print(valor, end = ' ')

for atrib in produto.keys():
    print(atrib, end = ' ')
