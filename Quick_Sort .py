def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        inicio = lista[0]
        menor = [i for i in lista[1:] if i <= inicio]
        maior = [i for i in lista[1:] if i > inicio]
        return quick_sort(menor) + [inicio] + quick_sort(maior)

'''teste'''
lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
quick_sort(lista)
print(quick_sort(lista))