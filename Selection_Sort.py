def selection_sort(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

'''teste'''
lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
print(f"Lista original:{lista}")
lista_ordenados = selection_sort(lista)
print(f"Lista ordenada:{lista_ordenados}")