saldo = 0 
numero_saques = 0
extrato = ""
menu = """
==== Selecione a operação desejada ====
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair
=======================================
"""

while True:

    escolha = input(menu)

    if escolha == "s": #saque
        print ("Você selecionou a opção de saque!")

        if numero_saques < 3:

            valor_sacado = float(input("Insira o valor que deseja sacar: R$"))
            
            if valor_sacado < saldo and valor_sacado <= 500:
                saldo -= valor_sacado
                numero_saques = numero_saques + 1
                extrato += f"Saque: R$ {valor_sacado:.2f}\n"
                print(f"Saque de R$ {valor_sacado:.2f} realizado com sucesso!")

            elif valor_sacado > 500 and valor_sacado > saldo:
                print("\nVocê não tem saldo suficiente para essa operação e o valor informado ultrpassa o limite de saque!")

            elif valor_sacado > 500:
                print("\nO valor informado ultrapassa o seu limite de saque!")

            else: 
                print("\nVocê não tem saldo suficiente para essa operação!") 

        else:
            print("\nVocê já atingiu o seu número diário de saques!")
            
    elif escolha == "d": #depósito

        print ("Você selecionou a opção de deposito!")

        valor_depositado = float(input("\nInsira o valor que deseja depositar: R$"))

        if valor_depositado > 0: 
            saldo += valor_depositado 
            print(f"\nO seu saldo atual é de: R${saldo:.2f}")
            extrato += f"Depositado: R$ {valor_depositado:.2f}\n"
            print(f"Depósito de R$ {valor_depositado:.2f} realizado com sucesso!")

        else:
            print("\nValor incorreto digitado, tente novamente.")

    elif escolha == "e": #extrato

        print("\nVocê selecionou a opção de extrato!")
        print("\n========== Extrato =========")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")

    elif escolha == "q":
        print("Sessão finalizada pelo usuário.")
        break

    else: 
        print ("\nOpção inválida, tente novamente.")    
