import random
import os 

from variaveis import numeros_random
from funcoes import calcular_primeiro_digito, calcular_segundo_digito

while True:

    #MENU DE OPÇÕES
    print("=== MENU DE OPÇÕES ===")
    print("[1] Digite 1 para GERAR CPF")
    print("[2] Digite 2 para VALIDAR CPF")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:


    # GERANDO OS 9 PRIMEIROS NÚMEROS
        for i in range(9):
            numeros_random.append(random.randint(0, 9))



        # PRIMEIRO DÍGITO VERIFICADOR
        primeiro_digito_verificador = calcular_primeiro_digito(
            numeros_random
        )

        numeros_random.append(primeiro_digito_verificador)



        # SEGUNDO DÍGITO VERIFICADOR
        segundo_digito_verificador = calcular_segundo_digito(
            numeros_random
        )



        # MOSTRANDO O CPF
        print("\nCPF = "
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
    else :
        print('Opção invalida')

    #RECOMEÇAR PROGRAMA
    input("\nPressione ENTER para voltar ao menu principal...")
    break
