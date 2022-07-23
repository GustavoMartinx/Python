from functools import reduce
# Map converts an list into another of the same size and applying someoperation on it
# Map converte uma lista em outra do mesmo tamanho e aplicando alguma operação nela

def score_sum(delta):
    def sum(nota):
        return nota + delta
    return sum

scores = [6.4, 7.2, 5.4, 8.4]

# scores_finais_1 = map(score_sum(1.5), scores)  # no video desse jeito. Pra mim, QUEBRADO
# scores_finais_2 = map(score_sum(1.6), scores)  # no video desse jeito. Pra mim, QUEBRADO

# for scores_finais_1 in map(score_sum, scores): # no video desse jeito. Pra mim, QUEBRADO
#     print(scores_finais_1)                     # no video desse jeito. Pra mim, QUEBRADO

print(list(map(score_sum(1.5), scores)))        # SOLUTION STACKOVERFLOW
print(list(map(score_sum(1.6), scores)))        # SOLUTION STACKOVERFLOW


# for i, nota in enumerate(scores):
#     scores[i] = nota + 1.5

# for i in range(len(scores)):
#     scores[i] = scores[i] + 1.5
#----------------------------------------------

# Reduce loops through all elements of a list calling a function
# Reduce percorre todos os elementos de uma lista, chamando uma funcao

def sum(a, b):
    return a + b

total = reduce(sum, scores, 0)
print(total)