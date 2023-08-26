#CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

numero = int(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'O dobro do numero {numero} é {dobro}')
print(f'O triplo do numero {numero} é {triplo}')
print(f'A raiz quadrada do numero {numero} é {raiz_quadrada:.2f}')