#2. Escreva um programa que leia do teclado duas matrizes de dimensões 2×2 e mostre na tela a soma dessas duas matrizes.

matriz = [[0 for x in range(2)] for x in range(2)]
m1 = 0
m2 = 0
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input('Digite um numero para adicionar a matriz: '))
print(f'matriz gerada = {matriz}')
print()
print('podemos apresentar de uma forma melhor!')
for y in range(2):
    print('| ',end='')
    for z in range(2):
        print(f'{matriz[y][z]} ', end='')
    print('|')
for i in range(1):
    m1 = matriz[i][0] * matriz[i][1]
for i in range(1,2):
    m2 = matriz[i][0] * matriz[i][1]
mult = m1 * m2
print(f'A multiplicação entre as matrizes = {mult}')