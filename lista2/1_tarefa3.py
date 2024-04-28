'''Tarefa 3
1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"e
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

lista = []

tel = str(input('Telofonou pra vitima?')).lower()
loc = str(input('Esteve no local do crime?')).lower()
mora = str(input('Mora perto da vitima?')).lower()
devia = str(input('Devia para a vitima?')).lower()
trabalho = str(input('Já trabalhou com a vitim?')).lower()
lista.extend([tel,loc,mora,devia,trabalho])
#para inserir todas os itens na lista usamos o metodo .extend()
# se fosse para inserir apenas um item usaria .append()

quant_sim = lista.count('sim')
#para contar quantas resposta sim tem em uma lista se usa metodo .count()

print('\n')
if quant_sim == 2:
    print('suspeito')

elif quant_sim >= 4:
    print('cumplice')

elif quant_sim == 5:
    print('assasino')

else:
    print('inocente')

print('\n')
