'''faça um vetor de 10 numeros inteiros e mostre-os na ordem inversa'''

vetor = []
for i in range(10):
    num = int(input(f'Digite o {i+1}° numero: '))
    vetor.append(num)
    
vetor.reverse()
print(vetor)
