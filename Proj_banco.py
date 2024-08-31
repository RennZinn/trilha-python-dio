menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
num_dep = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        print ("Depósito")
        
        valordep = float(input(print("Digite o valor do depósito: \n ==>")))
        if valordep < 0:
            print("Não foi possível realizar o depósito, recomeçe")
        else:
            num_dep = num_dep + 1
            saldo = saldo + valordep
            extrato += f"Depósito: R${valordep:.2f} \n "

    elif opcao == "s":
        print("Saque")
        saque = float(input(print("Qual o valor do saque? ")))
        if saque > 500:
            print("Não é possivel sacar mais de 500 reais.")
        elif numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingidos.")
        elif saldo < saque:
            print("Não possui dinheiro suficiente na conta. ")

        else: 
            numero_saques = numero_saques+ 1
            saldo = saldo - saque
            extrato += f"Saque: R${saque:.2f} \n"

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, selecione a desejada.")