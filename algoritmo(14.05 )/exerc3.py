#utilizando o enumerate
def buscasequencial(lista,chave):
    for indice,elemento in enumerate(lista):
            if elemento == chave:
                return indice
    return -1

chave = 45
lista = [20,5,15,24,67,1,45,78,21,11]
pos = buscasequencial(lista,chave)

if pos == -1:
    print("não encontrei")
else:
    print("a, chave, ",chave, "esta posição",pos)