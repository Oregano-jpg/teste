import os
import platform

saldo = float(1000)

def limpa_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    elif sistema == "Linux" or sistema == "Darwin":  # Darwin é o macOS
        os.system('clear')
    else:
        print("\n" * 100)  # Fallback para outros sistemas (rola a tela para baixo)


while (True) :
    limpa_tela()
    print("\n=== Menu de Operações ===")
    print("A. Ver Saldo")
    print("B. Saque")
    print("C. Depósito")
    print("D. Sair")
    opcao = str(input("Escolha uma opção entre A B C ou D para sair: ")).lower()

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
            print("Valor inválido")
    elif opcao == "d":
        break #sai do loop while e encerra o programa
    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...") # Mantém o resultado na tela até o usuário pressionar Enter 