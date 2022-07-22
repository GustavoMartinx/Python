from functools import reduce
# Map()  converte uma lista em outra do mesmo tamanho e aplicando alguma operação nela

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas = [6.4, 7.2, 5.4, 8.4]

# notas_finais_1 = map(somar_nota(1.5), notas)  # no video desse jeito. Pra mim, QUEBRADO
# notas_finais_2 = map(somar_nota(1.6), notas)  # no video desse jeito. Pra mim, QUEBRADO

# for notas_finais_1 in map(somar_nota, notas): # no video desse jeito. Pra mim, QUEBRADO
#     print(notas_finais_1)                     # no video desse jeito. Pra mim, QUEBRADO

print(list(map(somar_nota(1.5), notas)))        # SOLUCAO STACKOVERFLOW
print(list(map(somar_nota(1.6), notas)))        # SOLUCAO STACKOVERFLOW


# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
#----------------------------------------------

# Reduce()  percorre todos os elementos de uma lista, chamando uma funcao.

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)