#9. O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente, deve ser maior que Min.
# Em segui-da, preencher uma lista com todos os valores divisíveis por 7 contidos no intervalor fechado [Min, Max]. Exibir a lista resultante na tela.
min = int(input('Digite um valor inteiro: '))
max = int(input('\nDigite um valor maior que o anterior: '))
while max <= min:
    max = int(input('\nDigite um valor maior que o anterior: '))
L = []
for i in range(min,max):
    if i % 7 == 0:
        L.append(i)
print(f'Lista gerada = {L}')