def calcular_primeiro_digito(numeros):
    soma = 0

    for i in range(9):
        n = numeros[i]
        peso = 10 - i
        soma += n * peso

    resto = soma % 11

    if 11 - resto == 10 or 11 - resto == 11:
        return 0
    else:
        return 11 - resto


def calcular_segundo_digito(numeros):
    soma = 0

    for i in range(10):
        n = numeros[i]
        peso = 11 - i
        soma += n * peso

    resto = soma % 11

    if 11 - resto == 10 or 11 - resto == 11:
        return 0
    else:
        return 11 - resto