def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


# Assigning a function to a variable
# Atribuindo uma função à uma variável
add = sum
print(add(3, 4))


# Passing an function as parameters of another function
# Passando uma função como parâmetro de outra função
def arithmetic_operation(function, op1, op2):
    return function(op1, op2)


result = arithmetic_operation(sum, 1, 1)
print(result)


result = arithmetic_operation(sub, 1, 1)
print(result)


def partial_sum(a):
    def finish_sum(b):
        return a + b
    return finish_sum


fn = partial_sum(10)
final_result = fn(22)
print(final_result)