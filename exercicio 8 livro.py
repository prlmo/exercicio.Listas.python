#8. Escreva um programa que leia um número N (entre 0 e 50) e, em seguida, defina uma lista V preenchendo-a com N números inteiros aleatórios
# (utilizar a função randint).
# Exiba-a na tela. Inicie um laço no qual será feita a leitura de um número X e que termina quando X for zero.
# Pesquise se X está ou não na lista V e, caso esteja, elimine todas as suas ocorrências.
import random
N = int(input('Digite um numero entre 0 e 50: '))
while N > 50:
    try:
        if N < 0 or N > 50:
            N = int(input('\nDigite um numero entre 0 e 50: '))
        else:
            break
    except:
        print('não é possivel digitar caracteres!\n'
              'Tente novamente!\n')
        continue
V = []
for i in range(N):
    V.append(random.randint(0, 100))
print(f'Lista gerada: {V}')
x = int(input('Digite um numero para pesquisar na lista: '))
while x != 0:
    if x in V:
        print(f'{x} SIM, está na lista!\n')
    else:
        print(f'{x} NÃO, está na lista!\n')
    x = int(input('Digite um numero para pesquisar na lista: '))
    continue
print('\nFim!')