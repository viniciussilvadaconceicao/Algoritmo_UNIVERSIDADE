'''2 Escreva uma função recursiva que calcule a potência de um número x elevado a um
expoente n.'''

#função recursiva (if / else)
# poténcia é o resultado de um numero elevado 3² = resultado 9
#qualquer numero elevado a 0 da 1
# x = numero  / n = expoente 

def potência(x, n): #funçao 
    if n == 0:  #condição de base 
        return 1
    
    elif n > 0:
        return x *potência(x, n -1) #caso de expoente positivo 
    
    else:
        return 1 / potência(x, -n) #caso de expoente negativo

base = 3
expoente = 2
resultado = potência(base, expoente)
print(resultado)