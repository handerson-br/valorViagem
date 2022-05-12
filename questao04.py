#Escrever um programa responsável por calcular o valor pago pelo cliente em uma corrida realizada com o aplicativo. 
# O valor pago será calculado considerando a quantidade de minutos multiplicada pela taxa que varia de acordo com a quantidade 
# de minutos da corrida.J'Caso o tempo da corrida tenha sido menor ou igual a 5 minutos, a taxa será de R$ 3,00, por minuto, 
# caso o tempo seja maior que 5 minutos e menor que 10, a taxa cobrada será de R$ 2,00/por minuto e caso a corrida dure 10 ou
# mais minutos, a taxa cobrada será de R$ 1,00.

tempo = int(input("tempo de viagem: "))
if(tempo>10):
    taxa=1
if(tempo<=5):
    taxa=3  
if(tempo<10 and tempo>5):
    taxa=2      
valor= tempo*taxa
print(f"O Valor a ser pago é de : R$",valor)