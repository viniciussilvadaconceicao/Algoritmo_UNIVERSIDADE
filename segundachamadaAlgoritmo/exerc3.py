'''faça um programa que leia 8 numeros e informe a soma e a media dos numeros'''
numeros = []
soma = 0
cont = 0
for i in range(8):
    num = int(input(f'Digite o {i+1}° numero: '))
    numeros.append(num)
    soma += num
    cont += 1
    media = soma / cont
    
print(f'a soma desses numeros digitados da {soma} e a media é {media}')