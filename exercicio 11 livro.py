# 11. Faça um programa que leia um número inteiro N bem grande (acima de 5.000).
# Preencha uma lista de tamanho N com números inteiros aleatórios positivos. Em seguida, inicie um laço de pesquisa,
# no qual o valor a ser pesquisado deve ser lido do teclado, e o programa deve dizer se tal valor está ou não contido na lista, bem como dizer sua posição.
# No caso de várias ocorrências, exibir todas. O laço de pesquisa termina quando for digitado o zero. Use o algoritmo de busca sequencial.
from random import randint
N = int(input('Digite um numero acima de 5000: '))
while N < 5000:
    if N < 5000:
        N = int(input('\nDigite um numero acima de 5000: '))
L = []
for i in range(N):
    L.append(randint(0, N))
x = int(input('\nCaso desejar finalizar a pesquisa digite 0\n'
              'Digite um numero para pesquisar na lista: '))
while x != 0:
    if x in L:
        print(f'O valor {x} SIM, está na lista.\n')
        print(f'E a sua posição na lista é o índice: {L.index(x)}\n')
    else:
        print(f'\nO valor {x} NÃO está na lista. ')
    x = int(input('\nDigite um numero para pesquisar na lista: '))
print(f'Lista gerada =', L)
P = input("deseja pesquisar manualmente? \n"
            "S - sim\n"
            "N - não\n"
          ">> ")
while P == 's' or P == 's':
    if P == 'S' or P == 's':
        x = int(input('\nDigite o numero do índice para pesquisar na lista: '))
        print(L[x])
    else:
        print('\nFim')
    P = input("\ndeseja pesquisar manualmente? \n"
              "S - sim\n"
              "N - não\n"
              ">> ")
print('\n FIM DO PROGRAMA!!!')