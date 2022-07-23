from functools import reduce

students = [
    {'name': 'Ana', 'score': 7.2},
    {'name': 'Brenda', 'score': 8.1},
    {'name': 'Claudia', 'score': 8.7},
    {'name': 'Pedro', 'score': 6.4},
    {'name': 'Rafael', 'score': 6.7}
]

sum_ = lambda a, b: a + b

approved_students = [student for student in students if student['score'] >= 7]
approved_students_score = [student['score'] for student in approved_students]
total = reduce(sum_, approved_students_score, 0)

print(total / len(approved_students))
