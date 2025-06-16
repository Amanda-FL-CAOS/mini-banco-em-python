from datetime import datetime

menu = """

[1] Depositar
[2] Sacar
[3] Visualizar extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
número_saques = 0
LIMITE_SAQUES = 3

while True:
    opção = input(menu)
        
    if opção == "1":
        print("Opção depósito selecionada")
        valor_deposito =float(input ("digite o valor que deseja depositar: R$").replace(",", "."))

        if valor_deposito > 0:

            saldo += valor_deposito
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"[{agora}] Depósito: R$ {valor_deposito:.2f}")
            print("O deposito foi realizado com sucesso!")

        else:
            print("Depósito não realizado, por favor selecione um valor válido")

        print("O saldo atualizado é de R$", saldo)

    elif opção == "2":
        print("Opção Saque selecionada")
        valor_saque = float(input("Digite o valor que deseja sacar: R$").replace(",", "."))
        if valor_saque <= limite > 0 > saldo:
            número_saques += 1
            if número_saques >= LIMITE_SAQUES:
                print("O limite de saque diário já foi atingido")

            else:
                saldo -= valor_saque
                agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f"[{agora}] Saque: R$ {valor_saque:.2f}")
                print("O Saque foi realizado com sucesso!")
        else:
            print("Não foi possível realizar o saque. Valor inválido ou sem saldo na conta.")

        print("O saldo atualizado é de R$", saldo)

    elif opção == "3":
        print("\n===== EXTRATO =====")
        if extrato:
            for item in extrato:
                print(item,"\n => O saldo atualizado é de R$", saldo )
            
        else:
            print("Não foram realizadas movimentações.")


    elif opção == "0":
        print("Obrigado por usar o nosso sistema! ^-^")
        break