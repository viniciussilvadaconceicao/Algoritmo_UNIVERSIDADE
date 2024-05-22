#lista= [20,5,15,24,67,45,1,46,21,11]
def buscabinaria(lista,chave):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio
        if lista[meio] > chave:
            fim = meio - 1
        if lista[meio] < chave:
            inicio = meio + 1
    return-1

procurado = 45
lista = [20,5,15,24,67,45,1,46,21,11]
lista.sort()

resultado = buscabinaria(lista,procurado)
#chamada da função 

if resultado == -1:
    print("O elemento nao encontrado")
else:
    print("O elemento esta na posicao", resultado)