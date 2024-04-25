'''4. Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
 ou em galões de 3,6 litros, que custam R$ 25,00.
• Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o desperdício de tinta seja
menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto
é, considere latas cheias.'''

import math

metros_quadrados = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
litros_tinta = metros_quadrados / 6

lata = 18
galao = 3.6

preco_lata = 80
preco_galao = 25

# Calculando o número máximo de latas e galões necessários
quantidade_latas_max = math.ceil(litros_tinta / lata)
quantidade_galoes_max = math.ceil(litros_tinta / galao)

# Inicializando o custo mínimo com um valor alto inicialmente
custo_minimo = float('inf')
melhor_combinacao = None

# Verificando todas as combinações possíveis de latas e galões
for num_latas in range(quantidade_latas_max + 1):
    for num_galoes in range(quantidade_galoes_max + 1):
        litros_total = (num_latas * lata) + (num_galoes * galao)
        if litros_total >= litros_tinta:
            preco_total = (num_latas * preco_lata) + (num_galoes * preco_galao)
            if preco_total < custo_minimo:
                custo_minimo = preco_total
                melhor_combinacao = (num_latas, num_galoes)

# Exibindo a melhor combinação encontrada
if melhor_combinacao:
    num_latas, num_galoes = melhor_combinacao
    if num_latas > 0:
        print(f'A opção mais econômica é comprar {num_latas} latas', end='')
        if num_galoes > 0:
            print(f' e {num_galoes} galões.')
        else:
            print('.')
    elif num_galoes > 0:
        print(f'A opção mais econômica é comprar {num_galoes} galões.')
    print(f'O custo total será de R${custo_minimo:.2f}.')
else:
    print('Não foi possível encontrar uma combinação para cobrir a área especificada.')
