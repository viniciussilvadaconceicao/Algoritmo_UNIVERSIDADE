"""refaça a função sem utilizar lista [pos]"""

def buscasequencial(lista,chave):
    indice = 0
    for elemento in (lista):
            if elemento == chave:
                return indice
            indice += 1
    return -1

chave = 45
lista = [20,5,15,24,67,45,1,78,21,11]
pos = buscasequencial(lista,chave)

if pos == -1:
    print("não encontrei")
else:
    print("a, chave, ",chave, "esta posição",pos)