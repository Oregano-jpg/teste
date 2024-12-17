import os
saldo = float(1000)

print("\n=== Menu de Operações ===")
print("A. Ver Saldo")
print("B. Saque")
print("C. Depósito")
print("D. Sair")
opcao = str(input("Escolha uma opção entre A B C ou D para sair: ")).lower()

while (opcao!="d") :
    os.system('cls')
    if (opcao=="a"):
        print(f"O seu saldo é = R${saldo:.2f}" )
    elif(opcao == "b"):
        try:
            
            ValorDoSaque = float(input("Digite quanto quer Sacar:"))
            if (ValorDoSaque>saldo):
                print("Valor do saldo insuficiente")
            else:
                saldo-=ValorDoSaque
                print(f"Saque realizado com sucesso seu saldo restante é R${saldo:.2f}")
        except ValueError:
            print("Valor invalido")
    elif(opcao=="c"):
        try:
            ValorDoDeposito = float(input("Digite quanto quer Depositar:"))
            saldo+=ValorDoDeposito
            print(f"Deposito realizado com sucesso seu novo saldo é R${saldo:.2f}")
        except ValueError:
            print("Valor invalido")
    else:
        print("Opção invalida tente novamente")

    print("\n=== Menu de Operações ===")
    print("A. Ver Saldo")
    print("B. Saque")
    print("C. Depósito")
    print("D. Sair")
    opcao = str(input("Escolha uma opção entre A B C ou D para sair: ")).lower()
