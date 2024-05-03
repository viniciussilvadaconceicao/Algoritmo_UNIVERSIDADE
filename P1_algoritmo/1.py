'''11. Crie uma função chamada comprimentoMenor que recebe duas strings
como parâmetros e retorna True se o comprimento da primeira string for
menor do que o da segunda string, e False caso contrário.'''

def comprimentoMenor(str_1, str_2):
    return len(str_1) < len(str_2)


str_1 = 'titulo'
str_2 = 'rede'

print(comprimentoMenor(str_1, str_2))  

