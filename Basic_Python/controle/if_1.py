nota = float(input('Informe a nota do aluno: '))

if nota >= 9:
    print('Duas palavras: para bens!')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperacao')
elif nota >= 3.5:
    print('Recuperacao + Trabalho')
else:
    print('Reprovado')
print(nota)
