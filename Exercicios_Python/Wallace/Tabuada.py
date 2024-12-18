numero= int(input("Qual numero inteiro voce quer saber a Tabuada?\n"))
for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")