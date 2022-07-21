people = ['Mari', 'Gu']
adjective = ['Resilient', 'Funny']

for p in people:
    for a in adjective:
        print(f'{p} is {a}!')


for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2:
        continue
    print(i)

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('End!')