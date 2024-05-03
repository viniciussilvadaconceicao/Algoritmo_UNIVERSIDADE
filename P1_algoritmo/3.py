'''Crie uma função em Python que leia 80000 números e informe a média
dos números. Utilize Funções.'''
def calcular_media(n):
    soma = 0
    numero = float(input(f'Digite o número: '))
    soma = soma + numero
    media = soma / n
    return media

media = calcular_media(80000)

print(f'A média é: {media}')
