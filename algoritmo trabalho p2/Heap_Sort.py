def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[i] < lista[esquerda]:
        maior = esquerda

    if direita < n and lista[maior] < lista[direita]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_Sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

if __name__ == "__main__":
    lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
    heap_Sort(lista)
    print("Lista ordenada:")
    print(lista)