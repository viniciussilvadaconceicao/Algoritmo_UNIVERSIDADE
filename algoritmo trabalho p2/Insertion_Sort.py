def Insertion_Sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        '''Movendo os elementos de lista[0..i-1], que são maiores que a chave,
        para uma posição à frente da sua posição atual'''
        i = i-1
        while i >= 0 and chave < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = chave

'''teste'''
lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
Insertion_Sort(lista)
print(f"lista ordenado: {lista}")