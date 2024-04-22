'''6. Escreva uma função recursiva que encontre todos os anagramas de uma string'''
def anagrama(a, palavra):
    if a == '':
        print(palavra)
    else:
        for i in range(len(a)):
            anagrama(a[:i] + a[i+1:], palavra + a[i])

str_inicial = ""
anagrama("uva", str_inicial)
