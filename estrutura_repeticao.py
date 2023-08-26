''' for <nome variavel> in <interavel> 

# <nome variavel> é o nome da variavel que vai receber  os elementos do <interavel>
# <interavel> é o container de dados que vamos iterar.

Exemplo abaixo:'''

carros =['Celta', 'Corsa', 'Gol Bola', 'Fusca']

for carro in carros:
    print(carro)

'''while <condicao>: pode ser True ou False, a verificação de uma variavel, retorno de uma função e etc.
    #Bloco a ser executado'''

contador = 0
while contador < 11:
    print(f'Valor do contador é {contador}')
    contador += 1