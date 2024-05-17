import textwrap

menu2 = """
==== Selecione a operação desejada ====
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair
=======================================
"""

def menu():
    menu = """\n
    =============== Menu ==================
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [Cu] Criar usuário
    [Cc] Criar conta
    [Lc] Listar contas
    [q] Sair
    =======================================
    ==> """
    return input(textwrap.dedent(menu))


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0:
            if valor < saldo and valor <= 500:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            
            elif valor > limite and valor > saldo:
                print("\nVocê não tem saldo suficiente para essa operação e o valor informado ultrpassa o limite de saque!")

            elif valor > limite:
                print("\nO valor informado ultrapassa o seu limite de saque!")

            else: 
                print("\nVocê não tem saldo suficiente para essa operação!") 
        else:
            print("--- Valor informado é inválido! ---")

    else:
        print("\nVocê já atingiu o seu número de saques!")
    
    return saldo, extrato


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\nValor de R${valor} depositado!")
    else:
        print("--- Valor informado é inválido! ---")

    return saldo, extrato

def extrato (saldo, /, *, extrato):
    print("\n========== EXTRATO =========")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Já existe usuário com esse CPF! ---")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n--- Usuário não encontrado. Por favor, crie o usuário ---")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main ():
    agencia = "001"

    limite_saques = 3
    saque_maximo = 500
    saldo = 0 
    saques_realizados = 0
    extrato = ""
    contas = []
    usuarios = []

    while True:
        selecao = menu()

        if selecao == "s": 
            print ("Você selecionou a opção de saque!")

            valor = float(input("Insira o valor que deseja sacar: R$"))
            
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato, 
                limite = saque_maximo, 
                numero_saques = saques_realizados,
                limite_saques = limite_saques,
            )
        
        elif selecao == "d": 
            print ("Você selecionou a opção de deposito!")

            valor = float(input("\nInsira o valor que deseja depositar: R$"))
        
            saldo, extrato = deposito (saldo, valor, extrato)
        
        elif selecao == "e":
            print("\nVocê selecionou a opção de extrato!")

            extrato(saldo, extrato=extrato)
        
        elif selecao == "Cu" or selecao == "cu":
            print ("Você selecionou a opção de criar usuário!")

            criar_usuario(usuarios)

        elif selecao == "Cc" or selecao == "cc":
            print ("Você selecionou a opção de criar conta!")
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif selecao == "Lc" or selecao == "lc":
            print ("Você selecionou a opção de listar contas!")
            listar_contas(contas)

        elif selecao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main ()

