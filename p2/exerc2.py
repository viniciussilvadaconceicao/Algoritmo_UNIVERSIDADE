'''faça um programa que leia 10 numeros inteiros , calcule e mostre a quantidade de numeros pares'''
pares = list()
for i in range(10):
    num = int(input(f'Digite o {i+1}° numero: '))
    if num % 2 == 0:
        pares.append(num)

print(f'os numeros pares digitados foi:{pares}')