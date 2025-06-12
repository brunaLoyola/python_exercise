#Curso em video
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
valor = (km * 0.15) + (dias * 60)
print(f'O carro rodou {km} km e foi utilizado por {dias} dias, o valor a pagar é de R${valor:.2f}')
