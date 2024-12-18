import os
import math
consumoDoVeiculo = float
precoCombustivel = float
velocidadeMedia = float
custoTotal = float
##coletando os dados
while True:
    try :
        
        distancia = float(input("\nInsira a distancia da viagem em quilometros: \n"))
        os.system('cls')
        consumoDoVeiculo= float(input("\nInsira agora o consumo do veiculo em km/l: \n"))
        os.system('cls')
        precoCombustivel= float(input("\nInsira agora o preço do combustivel em R$ \n"))
        os.system('cls')
        velocidadeMedia = float(input("\n Agora insira a velocidade media pretendida em Km/h\n"))
        break
    except ValueError:
        print("Entrada invalida digite um numero")



#Calculos
combustivelGasto =distancia/consumoDoVeiculo
resultadoGasto = combustivelGasto*precoCombustivel

tempoEmHoras = math.floor(distancia/velocidadeMedia)
restoHoras = distancia/velocidadeMedia - tempoEmHoras
tempoMinutos = math.floor( 60* restoHoras)
restoMinuto = restoHoras * 60 - tempoMinutos
tempoSegundos= math.floor(restoMinuto*60)


#exibir os resultas
os.system('cls')
print(f"O Combustivel gasto será de {combustivelGasto:.2f}L \n O valor gasto será de R${resultadoGasto:.2f}\n")
print(f"O tempo de viagem será de : {tempoEmHoras} Hora(s), {tempoMinutos} Minuto(s), {tempoSegundos} Segundo(s)")