"""Escreva um programa que pergunte a quantidade de dias e a quantidade de Km percorridos por um carro alugado 
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias_alugados = int(input('Quantos dias foi alugado? '))
km_rodados = float(input('Quantos KM você percorreu? '))

valor_aluguel = (dias_alugados * 60) + (km_rodados * 0.15)

print(f'O valor a pagar é de R$ {valor_aluguel:.2f}')