import math
import os 
#coleta de dados 
os.system("cls")
distancia = float(input(f"insira a distancia da viagem ?\n")) 
os.system ("cls")
consumo_veiculo = float(input(f"qual é o consumo do veiculo em km/l ? \n"))
os.system("cls")
preco_combustivel = float(input(f"insira o preco do combustivel em R$?\n"))
os.system("cls")
velocidade_media = float(input(f"digite a velocidade media em que sera feito o trecho ?\n"))
# calculo 
cosbustivel_gasto = distancia / consumo_veiculo
resultado_da_gasto = cosbustivel_gasto *preco_combustivel
tempo_hora = distancia / velocidade_media
#divisao do tempo hora
resto_horas = distancia/velocidade_media - tempo_hora
#pega o resto em horas
tempo_hora = math.floor (distancia/velocidade_media)
# calculo 
tempo_minutos = math.floor (60*resto_horas )
#pega o resto dos minutos
resto_minuto = resto_horas * 60 - tempo_minutos
# pega o resto e subtrae o valor desejado como nos acimas para deixar apenas o que é desejado
tempo_sengundos = math.floor (resto_minuto*60)

# EXIBICAO 
os.system("cls")
print (f"esse é o total de combustivel gasto !{cosbustivel_gasto:.2f}L\n este é o resultado do gasto em R${resultado_da_gasto:.2f}")
print (f"este será o tempo gasto em horas{tempo_hora}\n tempo gasto em minutos{tempo_minutos}\n tempo gasto em segudos {tempo_sengundos}\n")
