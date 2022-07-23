# Lambda is a anonymous function (no name) used to define inline functions
# Lambda é uma função anônima (sem nome) usada para definir funções de única linha
from functools import reduce

students = [
    {'name': 'Ana', 'score': 7.2},
    {'name': 'Brenda', 'score': 8.1},
    {'name': 'Claudia', 'score': 8.7},
    {'name': 'Pedro', 'score': 6.4},
    {'name': 'Rafael', 'score': 6.7}
]

student_approved = lambda student: student['score'] >= 7
get_score = lambda student: student['score']
sum_ = lambda a, b: a + b

approved_students = list(filter(student_approved, students))
approved_students_score = list(map(get_score, approved_students))
total = reduce(sum_, approved_students_score, 0)

print(total / len(approved_students))
