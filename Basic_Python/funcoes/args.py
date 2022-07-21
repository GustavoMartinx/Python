def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):
    status = 'Aprovado(a)' if kwargs['nota'] >= 6 else 'Reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'
