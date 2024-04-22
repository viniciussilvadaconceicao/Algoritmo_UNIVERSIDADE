import math

def somatorio(n):
    soma = 0
    for i in range(1, n + 1):
        soma = soma + pow(i, 2)
    return soma

n = 3
resultado = somatorio(n)
print(resultado)
