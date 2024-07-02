def impares(lista):
    impares = list()
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    return impares

'''exemplo de lista'''
lista = [1,2,3,4,5,6,7,8,9,10]
print(impares(lista))