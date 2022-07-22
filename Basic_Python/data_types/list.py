# List
nums = [1, 2, 3]
print(type(nums))

# Parameter passed will be inserted in the list as the last element
# Parametro passado sera inserido na lista como ultimo elemento
nums.append(3)
nums.append(4)
nums.append(5)

# Size
# Tamanho
print(len(nums))

nums[3] = 100
# Insere o elemento -200 na posicao 0 deslocando os outros elementos
# Insert the element -200 in position 0 moving the other elements
nums.insert(0, -200)

# Access the last one of the list
# Acessa o ultimo elemento da lista
print(nums[-1])

print(nums)
