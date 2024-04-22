'''1 Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois
números inteiros a e b. '''
def mdc(a,b):
    if b == 0:
        return a 
    else:
        return mdc(b, a % b)
n1 = 24
n2 = 60
resultado = mdc (n1, n2 )
print(resultado)