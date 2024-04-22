'''3. Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for
"python", a função deve retornar "nohtyp".'''
#função recursiva é (if / else)

def inverta_string(a):# funçao
    if a == '':
        return a
    else:
        return inverta_string(a[1:])+ a[0]#Isso garante que a string seja invertida adequadamente.

str_inicial = "python" #variavel 
str_2 = inverta_string(str_inicial) #variavel
print(str_2)
