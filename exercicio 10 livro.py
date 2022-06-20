# 10. Escreva um programa que leia do teclado uma lista com N elementos.
# Em seguida, o programa deve eliminar os elementos que estiverem repetidos, mantendo apenas a primeira ocorrência de cada.
# Apresentar a lista resul-tante na tela. Os valores eliminados devem ser armazenados em outra lista que também deve ser exibida.
N = int(input('Qual vai ser o tamanho da lista? '))
L = []
E = []

for i in range(N):
    x = int(input('\nDigite os valores para preencher essa lista: '))
    if x not in L:
        L.append(x)
        continue
    else:
        E.append(x)

print(f'Lista gerada = {L}')
print(f'valores repetidos removidos da lista = {E}')