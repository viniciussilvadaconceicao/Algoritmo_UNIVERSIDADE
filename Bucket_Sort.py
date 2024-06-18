'''primeiro de tudo Criar uma lista de baldes vazios,
    depois distribuimos os elementos da lista de entrada nos baldes, 
    logo após ordenar os baldes e por fim concatena os baldes ordenados em uma única lista
    por fim concatena os baldes ordenados em uma única lista'''

def bucket_sort(lista):
    
    baldes = [[] for _ in range(len(lista))]

    for num in lista:
        indice = int(num * len(lista))
        baldes[indice].append(num)

    for balde in baldes:
        balde.sort()

    lista_ordenada = [num for balde in baldes for num in balde]

    return lista_ordenada

'''teste'''
'''é o correto usar números no intervalo entre (0, 1), pois utiliza num * len(lista) para determinar o índice do balde'''
lista = [0.21, 0.11, 0.8, 0.97, 0.1, 0.21, 0.1, 0.9, 0.22, 0.3]
lista_ordenada = bucket_sort(lista)
print(lista_ordenada)