import random

from variaveis import numeros_random
from funcoes import calcular_primeiro_digito, calcular_segundo_digito


# ==============================
# GERANDO OS 9 PRIMEIROS NÚMEROS
# ==============================

for i in range(9):
    numeros_random.append(random.randint(0, 9))


# ==============================
# PRIMEIRO DÍGITO VERIFICADOR
# ==============================

primeiro_digito_verificador = calcular_primeiro_digito(
    numeros_random
)

numeros_random.append(primeiro_digito_verificador)


# ==============================
# SEGUNDO DÍGITO VERIFICADOR
# ==============================

segundo_digito_verificador = calcular_segundo_digito(
    numeros_random
)


# ==============================
# MOSTRANDO O CPF
# ==============================

print(
    f'{numeros_random[0]}'
    f'{numeros_random[1]}'
    f'{numeros_random[2]}.'
    f'{numeros_random[3]}'
    f'{numeros_random[4]}'
    f'{numeros_random[5]}.'
    f'{numeros_random[6]}'
    f'{numeros_random[7]}'
    f'{numeros_random[8]}-'
    f'{primeiro_digito_verificador}'
    f'{segundo_digito_verificador}'
)