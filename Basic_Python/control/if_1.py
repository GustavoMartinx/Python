score = float(input('Enter the studant score: '))

if score >= 9:
    print('Duas palavras: para bens! :P')
    print('Honor Board')
elif score >= 7:
    print('Approved')
elif score >= 5.5:
    print('Recovery')
elif score >= 3.5:
    print('Recovery + Homework')
else:
    print('Disapproved')
print(score)
