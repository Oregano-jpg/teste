import os
os.system('cls')
numeros=[]
for i in range (10):
    numero=(int(input("digite um numero inteiro até 10 numeros\n")))
    numeros.append(numero)
    
for i, numeros in enumerate(numeros):
    resultado = numeros * 2
    print(f"{numero} x 2 = {resultado}")