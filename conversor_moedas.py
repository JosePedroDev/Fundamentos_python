#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quanto de dinheiro você tem na carteira: R$ '))
dolar = real / 8.50
euro = real / 12.70
libras = real / 18.50

print(f'Com o valor R$ {real} você pode comprar US$ {dolar:.2f} dolares')
print(f'Com o valor R$ {real} você pode comprar €  {euro:.2f} euros')
print(f'Com o valor R$ {real} você pode comprar £ {libras:.2f} libras')