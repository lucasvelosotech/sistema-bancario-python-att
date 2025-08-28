def exibir_menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.
    Recebe saldo, valor e extrato como argumentos posicionais.
    Retorna o novo saldo e o extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Recebe todos os argumentos de forma nomeada (keyword-only).
    Retorna o novo saldo, extrato atualizado e o novo número de saques.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Recebe saldo como argumento posicional e extrato como argumento nomeado.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")

def main():
    """Função principal que executa o sistema bancário."""
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()