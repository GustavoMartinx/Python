total = 0.0
score = 0
qte = 0

while score != -1:
    score = float(input('Enter the score. Or -1 to get out: '))
    if score != -1:
        qte += 1
        total += score

print(f'The class average is {total / qte}')
