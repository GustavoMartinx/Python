total = 0.0
nota = 0
qte = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qte += 1
        total += nota

print(f'A media da turma eh {total / qte}')
