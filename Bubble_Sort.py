'''O Bubble Sort é um algoritmo de ordenação que funciona comparando 
pares de elementos adjacentes na lista trocando-os de posição se estiverem na ordem errada.
 Processo esse que é repetido várias vezes até que a lista esteja ordenada.
'''

def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            return lista

'''teste'''
lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:")
for elemento in lista_ordenada:
    print(elemento)