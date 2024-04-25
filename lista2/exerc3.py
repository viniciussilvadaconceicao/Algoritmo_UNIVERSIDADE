'''3. Faça um programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math

metros_quadrados = float(input('Qual será o tamanho em metros quadrados da área a ser pintada: '))
litros_tinta = metros_quadrados / 3
quantidade_latas = math.ceil(litros_tinta / 18)
preco_total = quantidade_latas * 80
# Calculando o preço total
print(f"Quantidade de latas de tinta necessárias: {quantidade_latas}")
print(f"Preço total: R${preco_total:.2f}")