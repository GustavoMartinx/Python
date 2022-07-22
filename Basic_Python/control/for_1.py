# From 0 to 10 ignoring 10
# De 0 até 10, excluindo o 10
for i in range(10):
    print(i)

# From 1 to 11, ignoring 11
# De 1 até 11, excluindo o 11
for i in range(1, 11):
    print(i)

# From 1 to 100 from 10 to 10
# de 1 até 100 de 10 em 10
for i in range(1, 100, 10):
    print(i)

nums = [2, 4, 6, 8]
for n in nums:
    print(n, end = ' ')  # end=' ' print an space between the elements

text = 'Python is cool'
for letter in text:
    print(letter, end = '')

for n in {1, 2, 3, 4, 4, 4}:
    print(n, end = ' ')


product = {
    'name': 'Pen',
    'price': 8.00,
    'discount': 0.5
}

# Print everything in product (key and value)
# Imprime tudo do produto (chave e valor)
for key in product:
    print(key, product[key])

# Print everything in product (key and value)
# Imprime tudo do produto (chave e valor)
for key, value in product.items():
    print(key, value)

# Print all values of keys in product
# Imprime tudos os valores dos atributos do produto
for value in product.values():
    print(value, end = ' ')

# Print all keys in product
# Imprime tudos os atributos do produto
for key in product.keys():
    print(key, end = ' ')
