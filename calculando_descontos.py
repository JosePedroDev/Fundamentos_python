#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
valor_desconto = preco * 0.05
novo_preco = preco - valor_desconto

print(f'O produto custava R$ {preco:.2f} na promoção com o desconto de 5%, você ganhou R$ {valor_desconto:.2f} de desconto, o produto vai custar R$ {novo_preco:.2f}')