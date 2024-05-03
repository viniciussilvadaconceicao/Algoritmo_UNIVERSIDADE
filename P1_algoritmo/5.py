'''5. Crie uma função recursiva que receba um número inteiro positivo N e
calcule o somatório dos números de 1 a N.'''
def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)

n = 5
resultado = somatorio(n)
print(f'O somatório dos números de 1 a, {n}, é {resultado}')
