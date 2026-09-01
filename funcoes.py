"""Funções para cálculo dos dígitos verificadores de um CPF."""


def calcular_digito_verificador(numeros, pesos):
    """Calcula um dígito verificador a partir de uma lista de números e pesos."""
    soma = sum(numero * peso for numero, peso in zip(numeros, pesos))
    resto = soma % 11
    digito = 11 - resto
    return 0 if digito >= 10 else digito


def calcular_primeiro_digito(numeros):
    """Calcula o 1º dígito verificador a partir dos 9 primeiros números do CPF."""
    pesos = range(10, 1, -1)  # 10, 9, ..., 2
    return calcular_digito_verificador(numeros[:9], pesos)


def calcular_segundo_digito(numeros):
    """Calcula o 2º dígito verificador a partir dos 10 primeiros números do CPF."""
    pesos = range(11, 1, -1)  # 11, 10, ..., 2
    return calcular_digito_verificador(numeros[:10], pesos)