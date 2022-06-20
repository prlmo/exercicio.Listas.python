# 7. Escreva um programa que leia um número N obrigatoriamente entre 0 e 50 e, em seguida,
# leia N números reais em uma lista A.O programa deve separar os valores lidos em A em outras duas listas NEG e POS:
# a primeira contendo somente os valores negativos e a segunda contendo os valores positivos e zero.
# Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma
N = int(input('Digite um numero entre 0 e 50: '))
while True:
    try:
        if N > 50 or N < 0:
            print(f'{N} é inválido.\n'
                  f'Por favor, digite corretamente')
            N = int(input('\nDigite um numero entre 0 e 50: '))
        else:
            break
    except:
        print('Inválido!')
A = []
NEG = []
POS = []
c = N+1
for i in range(0,N+1):
    x = float(input(f'Falta {c} numeros reais para adicionar a lista: '))
    c -= 1
    A.append(x)
    if x < 0:
        NEG.append(x)
    else:
        POS.append(x)
print(f'Lista gerada tem {len(A)} valores.\n'
      f'Sendo entre eles.\n'
      f'Os negativos = {NEG}\n'
      f'E os positivos = {POS}')