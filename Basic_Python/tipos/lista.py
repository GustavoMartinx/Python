nums = [1, 2, 3] # Lista
print(type(nums))

nums.append(3) # Parametro passado sera inserido na lista como ultimo elemento
nums.append(4)
nums.append(5)
print(len(nums)) # len() tamanho

nums[3] = 100
nums.insert(0, -200) # Insere o elemento -200 na posicao 0 deslocando os outros elementos

print(nums[-1]) # Acessa o ultimo elemento da lista

print(nums)
