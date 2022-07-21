# def soma(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# somar = soma
# print(somar(3, 4))


# def operacao_aritmetica(funcao, op1, op2):
#     return funcao(op1, op2)

# resultado = operacao_aritmetica(soma, 1, 1)
# print(resultado)


# resultado = operacao_aritmetica(subtracao, 1, 1)
# print(resultado)


def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

fn = soma_parcial(10)
resultado_final = fn(22)
print(resultado_final)