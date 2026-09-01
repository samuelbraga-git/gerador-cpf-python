import random

from funcoes import calcular_primeiro_digito, calcular_segundo_digito


def gerar_cpf():
    
    """Gera um CPF aleatório válido e o exibe formatado."""
    numeros = [random.randint(0, 9) for _ in range(9)]

    primeiro_digito = calcular_primeiro_digito(numeros)
    numeros.append(primeiro_digito)

    segundo_digito = calcular_segundo_digito(numeros)
    numeros.append(segundo_digito)

    cpf = (
        f"{numeros[0]}{numeros[1]}{numeros[2]}."
        f"{numeros[3]}{numeros[4]}{numeros[5]}."
        f"{numeros[6]}{numeros[7]}{numeros[8]}-"
        f"{numeros[9]}{numeros[10]}"
    )
    print(f"\nCPF gerado: {cpf}")


def verificar_cpf():
    """Lê um CPF do usuário e informa se ele é válido ou não."""
    cpf_digitado = input("\nDigite o CPF (com ou sem pontuação): ").strip()
    digitos = [caractere for caractere in cpf_digitado if caractere.isdigit()]

    if len(digitos) != 11:
        print("CPF inválido: é necessário informar 11 dígitos.")
        return

    numeros = [int(digito) for digito in digitos]

    primeiro_digito_calculado = calcular_primeiro_digito(numeros)
    segundo_digito_calculado = calcular_segundo_digito(
        numeros[:9] + [primeiro_digito_calculado]
    )

    cpf_valido = (
        numeros[9] == primeiro_digito_calculado
        and numeros[10] == segundo_digito_calculado
    )

    print("CPF VÁLIDO" if cpf_valido else "CPF INVÁLIDO")


def exibir_menu():
    print("\n=== MENU DE OPÇÕES ===")
    print("[1] Gerar CPF")
    print("[2] Verificar CPF")
    print("[0] Sair")


def main():
    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if opcao == 1:
            gerar_cpf()
        elif opcao == 2:
            verificar_cpf()
        elif opcao == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

        if opcao in (1, 2):
            input("\nPressione ENTER para voltar ao menu principal...")


if __name__ == "__main__":
    main()