'''5. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro
positivo.'''
def soma(a, b):#função
    if b == 0:  #condição
        return a
    else:
        return soma(a + 1, b - 1) 

a = 6 #variavel
b = 4 #variavel
resultado = soma(a, b)
print(resultado)
